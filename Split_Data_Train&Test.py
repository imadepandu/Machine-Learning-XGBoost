import pandas as pd
import os

# Konfigurasi
NLAGS = 5
MA_WINDOWS = [3, 5]
TRAIN_RATIO = 0.8

# input
df = pd.read_csv("DATA 5 SAHAM TERBESAR TERPERCAYA DAN TERGILA.csv", sep=';')
stocks = ["BBCA", "TPIA", "TLKM", "BRPT", "ASII"]

# output
os.makedirs("DATA TRAINING DAN TESTING", exist_ok=True)

# MEMBUAT LAG & MOVING AVERAGE
for stock in stocks:
    print(f"Processing fitur untuk {stock} ...")

    # Copy kolom harga
    series = df[[stock]].copy()

    # Buat lag
    for lag in range(1, NLAGS + 1):
        series[f"{stock}_lag{lag}"] = series[stock].shift(lag)

    # Buat Moving Average
    for w in MA_WINDOWS:
        series[f"{stock}_MA{w}"] = series[stock].rolling(window=w).mean()

    # Hapus baris NA pertama
    series.dropna(inplace=True)

    # Target adalah harga hari ini
    y = series[stock]
    X = series.drop(columns=[stock])

    # Split train-test
    split_idx = int(len(series) * TRAIN_RATIO)
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

    # Simpan CSV
    X_train.to_csv(f"DATA TRAINING DAN TESTING/X_train_{stock}.csv", index=False)
    X_test.to_csv(f"DATA TRAINING DAN TESTING/X_test_{stock}.csv", index=False)
    y_train.to_csv(f"DATA TRAINING DAN TESTING/y_train_{stock}.csv", index=False)
    y_test.to_csv(f"DATA TRAINING DAN TESTING/y_test_{stock}.csv", index=False)

    print(f"✓ {stock} selesai. Train: {X_train.shape}, Test: {X_test.shape}")

print("\n========================================================")
print("      SELURUH DATA TRAIN-TEST BERHASIL DIBUAT")
print("========================================================")
