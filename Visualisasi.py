import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Gunakan style visual yang bersih
sns.set(style="whitegrid")

BASE_DIR = "HASIL XGBOOST"
OUTPUT_DIR = "HASIL VISUALISASI"
STOCKS = ["BBCA", "TPIA", "TLKM", "BRPT", "ASII"]

# Buat folder output jika belum ada
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data(stock):
    folder = f"{BASE_DIR}/{stock}"
    df_train = pd.read_csv(f"{folder}/PrediksiTrain_{stock}.csv")
    df_test = pd.read_csv(f"{folder}/PrediksiTest_{stock}.csv")
    df_fi = pd.read_csv(f"{folder}/FeatureImportance_{stock}.csv")
    return df_train, df_test, df_fi


def save_plot(fig, filepath):
    fig.savefig(filepath, dpi=300, bbox_inches="tight")
    plt.close(fig)


def visualize_stock(stock):
    print(f"Processing {stock} ...")

    df_train, df_test, df_fi = load_data(stock)

    stock_dir = f"{OUTPUT_DIR}/{stock}"
    os.makedirs(stock_dir, exist_ok=True)

    # Train Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_train.index, df_train["Actual_Train"], label="Actual Train", linewidth=2)
    ax.plot(df_train.index, df_train["Predicted_Train"], label="Predicted Train", linewidth=2)
    ax.set_title(f"{stock} - Actual vs Predicted (Train)")
    ax.legend()
    save_plot(fig, f"{stock_dir}/Train_Plot_{stock}.png")

    # Test Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_test.index, df_test["Actual_Test"], label="Actual Test", linewidth=2)
    ax.plot(df_test.index, df_test["Predicted_Test"], label="Predicted Test", linewidth=2)
    ax.set_title(f"{stock} - Actual vs Predicted (Test)")
    ax.legend()
    save_plot(fig, f"{stock_dir}/Test_Plot_{stock}.png")

    # Feature Importance
    fig, ax = plt.subplots(figsize=(8, 5))
    df_fi.sort_values("Importance", ascending=True).plot.barh(
        x="Feature", y="Importance", ax=ax, color="darkblue"
    )
    ax.set_title(f"{stock} - Feature Importance")
    save_plot(fig, f"{stock_dir}/FeatureImportance_{stock}.png")

    # Scatter Plot (Actual vs Predicted)
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.scatterplot(
        x=df_test["Actual_Test"], y=df_test["Predicted_Test"], ax=ax, s=40
    )
    ax.set_title(f"{stock} - Scatter: Actual vs Predicted")
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    save_plot(fig, f"{stock_dir}/Scatter_{stock}.png")

    # Error Histogram
    df_test["Error"] = df_test["Actual_Test"] - df_test["Predicted_Test"]
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df_test["Error"], bins=25, kde=True, ax=ax, color="red")
    ax.set_title(f"{stock} - Error Distribution (Test)")
    save_plot(fig, f"{stock_dir}/ErrorHist_{stock}.png")

    print(f"✓ Visualizations saved for {stock}")

# Gabungkan 5 saham dalam satu plot (TRAIN)
print("\nMembuat plot gabungan Train untuk 5 saham...")

fig, axes = plt.subplots(5, 1, figsize=(14, 18), sharex=False)

for i, stock in enumerate(STOCKS):
    df_train, _, _ = load_data(stock)

    axes[i].plot(df_train.index, df_train["Actual_Train"], label="Actual Train", linewidth=2)
    axes[i].plot(df_train.index, df_train["Predicted_Train"], label="Predicted Train", linewidth=2)

    axes[i].set_title(f"{stock} - Train Actual vs Predicted")
    axes[i].legend()

plt.tight_layout()
save_plot(fig, f"{OUTPUT_DIR}/Combined_Train_AllStocks.png")

print("✓ Combined Train plot saved.")

# Gabungkan 5 saham dalam satu plot (TEST)
print("Membuat plot gabungan Test untuk 5 saham...")

fig, axes = plt.subplots(5, 1, figsize=(14, 18), sharex=False)

for i, stock in enumerate(STOCKS):
    _, df_test, _ = load_data(stock)

    axes[i].plot(df_test.index, df_test["Actual_Test"], label="Actual Test", linewidth=2)
    axes[i].plot(df_test.index, df_test["Predicted_Test"], label="Predicted Test", linewidth=2)

    axes[i].set_title(f"{stock} - Test Actual vs Predicted")
    axes[i].legend()

plt.tight_layout()
save_plot(fig, f"{OUTPUT_DIR}/Combined_Test_AllStocks.png")

print("✓ Combined Test plot saved.")

# LOOP
if __name__ == "__main__":
    print("=========================================")
    print("  GENERATING VISUALIZATION IMAGES")
    print("=========================================\n")

    for stock in STOCKS:
        visualize_stock(stock)

    print("\n=========================================")
    print("     ALL VISUALIZATIONS GENERATED")
    print("=========================================")
    print(f"Saved in folder: {OUTPUT_DIR}")
