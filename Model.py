import pandas as pd
import os
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Folder Utama 
INPUT_DIR = "DATA TRAINING DAN TESTING"
OUTPUT_DIR = "HASIL XGBOOST"
os.makedirs(OUTPUT_DIR, exist_ok=True)

stocks = ["BBCA", "TPIA", "TLKM", "BRPT", "ASII"]

# PARAMETER 
model_params = dict(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=3,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_lambda=2.0,
    min_child_weight=3,
    objective='reg:squarederror',
    random_state=42,
    verbosity=0
)

print("\nTraining Models...\n")

# TRAINING MODEL PER SAHAM
for stock in stocks:

    try:
        # Folder khusus saham
        stock_dir = f"{OUTPUT_DIR}/{stock}"
        os.makedirs(stock_dir, exist_ok=True)

        # Load train-test
        X_train = pd.read_csv(f"{INPUT_DIR}/X_train_{stock}.csv")
        X_test = pd.read_csv(f"{INPUT_DIR}/X_test_{stock}.csv")
        y_train = pd.read_csv(f"{INPUT_DIR}/y_train_{stock}.csv").values.ravel()
        y_test = pd.read_csv(f"{INPUT_DIR}/y_test_{stock}.csv").values.ravel()

        # Train model
        model = XGBRegressor(**model_params)
        model.fit(X_train, y_train)

        # Predict
        pred_train = model.predict(X_train)
        pred_test = model.predict(X_test)

        # Metrics
        rmse_train = mean_squared_error(y_train, pred_train) ** 0.5
        rmse_test = mean_squared_error(y_test, pred_test) ** 0.5

        metrics_train = {
            "RMSE": rmse_train,
            "MAE": mean_absolute_error(y_train, pred_train),
            "R2": r2_score(y_train, pred_train)
        }

        metrics_test = {
            "RMSE": rmse_test,
            "MAE": mean_absolute_error(y_test, pred_test),
            "R2": r2_score(y_test, pred_test)
        }

        # Simpan Output
        pd.DataFrame({
            "Actual_Train": y_train,
            "Predicted_Train": pred_train
        }).to_csv(f"{stock_dir}/PrediksiTrain_{stock}.csv", index=False)

        pd.DataFrame({
            "Actual_Test": y_test,
            "Predicted_Test": pred_test
        }).to_csv(f"{stock_dir}/PrediksiTest_{stock}.csv", index=False)

        pd.DataFrame([metrics_train]).to_csv(f"{stock_dir}/MetricsTrain_{stock}.csv", index=False)
        pd.DataFrame([metrics_test]).to_csv(f"{stock_dir}/MetricsTest_{stock}.csv", index=False)

        fi = pd.DataFrame({
            "Feature": X_train.columns,
            "Importance": model.feature_importances_
        })
        fi.to_csv(f"{stock_dir}/FeatureImportance_{stock}.csv", index=False)

        model.save_model(f"{stock_dir}/Model_{stock}.json")

        with open(f"{stock_dir}/Summary_{stock}.txt", "w") as f:
            f.write(f"SUMMARY MODEL {stock}\n\n")
            f.write("=== TRAIN METRICS ===\n")
            for k, v in metrics_train.items():
                f.write(f"{k}: {v}\n")
            f.write("\n=== TEST METRICS ===\n")
            for k, v in metrics_test.items():
                f.write(f"{k}: {v}\n")

        print(f"Training {stock} ... done.")

    except Exception as e:
        print(f"ERROR training {stock}: {e}")

print("\nAll models saved in:", OUTPUT_DIR)
