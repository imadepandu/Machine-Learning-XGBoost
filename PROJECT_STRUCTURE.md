# 📁 Struktur Proyek

Dokumentasi lengkap tentang struktur folder dan file dalam proyek ini.

## 📂 Struktur Folder

```
prediksi-harga-saham-xgboost/
│
├── 📄 Dokumentasi
│   ├── README.md                    # Dokumentasi utama
│   ├── CONTRIBUTING.md              # Panduan kontribusi
│   ├── SETUP.md                     # Panduan setup
│   ├── PROJECT_STRUCTURE.md         # File ini
│   └── LICENSE                      # Lisensi MIT
│
├── 📊 Data
│   ├── DATA 5 SAHAM TERBESAR TERPERCAYA DAN TERGILA.csv  # Dataset utama
│   └── DATA 5 SAHAM FINAL.csv       # Dataset setelah preprocessing
│
├── 📓 Notebook
│   └── Complete_Analysis.ipynb      # Notebook lengkap (Eksplorasi → Visualisasi)
│
├── 🐍 Scripts Python
│   ├── Eksplorasi_Data.py           # Eksplorasi data
│   ├── Split_Data_Train&Test.py     # Feature engineering & split
│   ├── Model.py                      # Training model
│   ├── Prediksi.py                  # Prediksi masa depan
│   └── Visualisasi.py                # Visualisasi hasil
│
├── 📦 Konfigurasi
│   ├── requirements.txt              # Dependencies Python
│   └── .gitignore                    # File yang diabaikan Git
│
├── 📂 Output Folders (Dibuat otomatis saat eksekusi)
│   │
│   ├── DATA TRAINING DAN TESTING/   # Data train-test split
│   │   ├── X_train_BBCA.csv
│   │   ├── X_test_BBCA.csv
│   │   ├── y_train_BBCA.csv
│   │   ├── y_test_BBCA.csv
│   │   └── ... (untuk 5 saham)
│   │
│   ├── HASIL XGBOOST/                # Hasil training model
│   │   ├── BBCA/
│   │   │   ├── Model_BBCA.json
│   │   │   ├── MetricsTrain_BBCA.csv
│   │   │   ├── MetricsTest_BBCA.csv
│   │   │   ├── PrediksiTrain_BBCA.csv
│   │   │   ├── PrediksiTest_BBCA.csv
│   │   │   ├── FeatureImportance_BBCA.csv
│   │   │   └── Summary_BBCA.txt
│   │   ├── TPIA/
│   │   ├── TLKM/
│   │   ├── BRPT/
│   │   └── ASII/
│   │
│   ├── HASIL PREDIKSI/               # Prediksi masa depan
│   │   ├── BBCA_future_12w.csv
│   │   ├── BBCA_future_12w.png
│   │   └── ... (untuk 5 saham)
│   │
│   └── HASIL VISUALISASI/            # Visualisasi hasil
│       ├── BBCA/
│       │   ├── Train_Plot_BBCA.png
│       │   ├── Test_Plot_BBCA.png
│       │   ├── FeatureImportance_BBCA.png
│       │   ├── Scatter_BBCA.png
│       │   └── ErrorHist_BBCA.png
│       ├── TPIA/
│       ├── TLKM/
│       ├── BRPT/
│       ├── ASII/
│       ├── Combined_Train_AllStocks.png
│       └── Combined_Test_AllStocks.png
```

## 📝 Deskripsi File

### Dokumentasi
- **README.md**: Dokumentasi utama proyek, panduan instalasi dan penggunaan
- **CONTRIBUTING.md**: Panduan untuk kontributor
- **SETUP.md**: Panduan setup dan instalasi
- **GITHUB_SETUP.md**: Panduan publish ke GitHub
- **LICENSE**: Lisensi MIT

### Data
- **DATA 5 SAHAM TERBESAR TERPERCAYA DAN TERGILA.csv**: Dataset utama dengan data harga saham
- **DATA 5 SAHAM FINAL.csv**: Dataset setelah preprocessing (dibuat oleh Eksplorasi_Data.py)

### Scripts
- **Eksplorasi_Data.py**: 
  - Load data
  - Statistik deskriptif
  - Cek missing values
  - Deteksi outlier
  
- **Split_Data_Train&Test.py**:
  - Feature engineering (lag & moving average)
  - Split data train-test (80:20)
  - Simpan ke folder DATA TRAINING DAN TESTING
  
- **Model.py**:
  - Training model XGBoost untuk 5 saham
  - Evaluasi metrics (RMSE, MAE, R²)
  - Simpan model dan hasil ke HASIL XGBOOST
  
- **Prediksi.py**:
  - Load model yang sudah di-train
  - Prediksi 12 minggu ke depan
  - Simpan prediksi dan plot ke HASIL PREDIKSI
  
- **Visualisasi.py**:
  - Visualisasi hasil training dan testing
  - Plot feature importance, scatter, error distribution
  - Simpan ke HASIL VISUALISASI

### Notebook
- **Complete_Analysis.ipynb**: Notebook lengkap yang menggabungkan semua langkah dengan output di terminal

## 🔄 Alur Kerja

```
1. Eksplorasi Data
   ↓
2. Feature Engineering & Split
   ↓
3. Training Model
   ↓
4. Prediksi Masa Depan
   ↓
5. Visualisasi
```

## 📊 Output yang Dihasilkan

### Model Files
- Model JSON untuk setiap saham
- Metrics training dan testing
- Feature importance
- Summary model

### Prediksi
- CSV file dengan prediksi 12 minggu
- Plot visualisasi prediksi

### Visualisasi
- Plot actual vs predicted (train & test)
- Feature importance chart
- Scatter plot
- Error distribution histogram
- Combined plots untuk semua saham

## 💡 Tips

1. **Jalankan script secara berurutan** untuk hasil yang konsisten
2. **Gunakan notebook** untuk eksplorasi interaktif
3. **Backup folder output** sebelum menjalankan ulang
4. **Periksa disk space** karena output bisa besar




