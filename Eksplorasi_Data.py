import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("DATA 5 SAHAM TERBESAR TERPERCAYA DAN TERGILA.csv", sep=';')

print("=== STATISTIKA DESKRIPTIF ===")
print(df.describe())

print("=== CEK MISSING VALUE ===")
print(df.isnull().sum())
print("Total missing value:", df.isnull().sum().sum())

def tampilkan_outlier(data):
    for col in data.columns[1:]:  
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1

        Batas_Bawah = Q1 - 1.5 * IQR
        Batas_Atas = Q3 + 1.5 * IQR

        outlier_df = data[(data[col] < Batas_Bawah) | (data[col] > Batas_Atas)]

        if not outlier_df.empty:
            print(f"\n===== Outlier pada kolom {col} =====")
            print(f"Jumlah outlier: {len(outlier_df)}")
            print(outlier_df[['Date', col]].reset_index(drop=True))
        else:
            print(f"\nTidak ada outlier pada kolom {col}.")

print("=== OUTLIER  ===")
tampilkan_outlier(df)

df_final = df.copy()

# Simpan file
output = "DATA 5 SAHAM FINAL.csv"
df_final.to_csv(output, index=False)

print("\n=== FILE BERHASIL DISIMPAN ===")
print("Lokasi:", output)
