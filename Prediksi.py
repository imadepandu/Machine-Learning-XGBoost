import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta
from xgboost import XGBRegressor

# Konfigurasi
DATA_FILE = "DATA 5 SAHAM FINAL.csv"
STOCKS = ["BBCA", "TPIA", "TLKM", "BRPT", "ASII"]
NLAGS = 5
MA_WINDOWS = [3, 5]
HORIZON = 12   # 12 weeks ahead
MODEL_FOLDER = "HASIL XGBOOST"
OUT_FOLDER = "HASIL PREDIKSI"
PLOT_DPI = 200

os.makedirs(OUT_FOLDER, exist_ok=True)

# HELPERS 
def load_models(stock):
    model_path = os.path.join(MODEL_FOLDER, stock, f"Model_{stock}.json")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    m = XGBRegressor()
    m.load_model(model_path)
    return m

def make_feature_row(stock, history_prices):
    """
    history_prices: list or 1d-array of historical prices ordered oldest...latest
    We expect last element = price_t (most recent observed).
    """
    row = {}
    # ensure we have at least NLAGS entries; if not, pad with repeated first value
    hist = list(history_prices)
    if len(hist) < NLAGS:
        # pad at left with earliest value
        pad = [hist[0]] * (NLAGS - len(hist))
        hist = pad + hist

    # lag_1 .. lag_N where lag_1 = price_t (most recent)
    for l in range(1, NLAGS + 1):
        # lag_l is element from end: -l
        row[f"{stock}_lag{l}"] = hist[-l]

    # MA windows computed on last available values (including predicted ones when recursive)
    for w in MA_WINDOWS:
        window_vals = hist[-w:] if len(hist) >= w else hist  # if not enough, use all
        row[f"{stock}_MA{w}"] = float(np.mean(window_vals)) if len(window_vals) > 0 else 0.0

    return row

def generate_future_dates(last_date, n_weeks):
    # treat data as weekly; add 7 days each step
    return [last_date + timedelta(weeks=i) for i in range(1, n_weeks+1)]

# MAIN
def main():
    # load data
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Historical data file not found: {DATA_FILE}")

    df_all = pd.read_csv(DATA_FILE, parse_dates=["Date"])
    df_all = df_all.sort_values("Date").reset_index(drop=True)

    for stock in STOCKS:
        print(f"Processing forecast for {stock} ...")

        # check model
        model_dir = os.path.join(MODEL_FOLDER, stock)
        if not os.path.isdir(model_dir):
            print(f"  -> Skip {stock}: model folder not found: {model_dir}")
            continue
        model_path = os.path.join(model_dir, f"Model_{stock}.json")
        if not os.path.exists(model_path):
            print(f"  -> Skip {stock}: model file not found: {model_path}")
            continue

        # load model
        model = XGBRegressor()
        model.load_model(model_path)

        # get historical price series for this stock
        if stock not in df_all.columns:
            print(f"  -> Skip {stock}: column '{stock}' not found in data file.")
            continue

        price_series = df_all[["Date", stock]].dropna().copy()
        price_series = price_series.sort_values("Date").reset_index(drop=True)

        if price_series.shape[0] < 1:
            print(f"  -> Skip {stock}: not enough data.")
            continue

        # prepare history list of prices (oldest ... latest)
        history = list(price_series[stock].astype(float).values)

        last_date = price_series["Date"].iloc[-1]
        future_dates = generate_future_dates(last_date, HORIZON)

        preds = []
        # recursive forecasting
        hist_for_pred = history.copy()  # will be appended with predictions
        for h in range(HORIZON):
            feat = make_feature_row(stock, hist_for_pred)
            # model expects columns in the same order as training X; create DataFrame with single row
            X_row = pd.DataFrame([feat])
            # If model was trained with different column order, XGBoost accepts by column names -> ok
            yhat = model.predict(X_row)[0]
            preds.append(float(yhat))
            # append predicted price to history for next step
            hist_for_pred.append(float(yhat))

        # Save CSV
        out_df = pd.DataFrame({
            "Date": future_dates,
            "Predicted": preds
        })
        csv_path = os.path.join(OUT_FOLDER, f"{stock}_future_{HORIZON}w.csv")
        out_df.to_csv(csv_path, index=False, date_format="%Y-%m-%d")
        print(f"  -> Saved CSV: {csv_path}")

        # Plot: include last N_actual points + future predictions
        N_actual = min(36, len(history))  # show up to last 36 weeks of actual
        actual_dates = list(price_series["Date"].iloc[-N_actual:])
        actual_prices = history[-N_actual:]

        # build combined series for plotting
        plot_dates = actual_dates + future_dates
        plot_prices_actual = actual_prices + [None]*len(future_dates)
        plot_prices_pred = [None]*len(actual_dates) + preds

        plt.figure(figsize=(10,5))
        plt.plot(plot_dates, plot_prices_actual, label="Actual (recent)", linewidth=2)
        plt.plot(plot_dates, plot_prices_pred, label=f"Predicted next {HORIZON}w", linewidth=2, linestyle="--")
        plt.scatter(future_dates, preds, color="red", s=30)
        plt.title(f"{stock} - Forecast {HORIZON} weeks")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()

        png_path = os.path.join(OUT_FOLDER, f"{stock}_future_{HORIZON}w.png")
        plt.savefig(png_path, dpi=300)
        plt.close()
        print(f"  -> Saved Plot: {png_path}")

    print("\nAll forecasts done. Files saved in:", OUT_FOLDER)

if __name__ == "__main__":
    main()
