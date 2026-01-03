# 📈 Prediksi Harga Saham dengan XGBoost

Proyek Machine Learning untuk memprediksi harga saham 5 perusahaan terbesar di Indonesia menggunakan algoritma XGBoost. Proyek ini mencakup eksplorasi data, feature engineering, model training, prediksi masa depan, dan visualisasi hasil.

## 📋 Daftar Isi

- [Deskripsi](#-deskripsi)
- [Fitur](#-fitur)
- [Dataset](#-dataset)
- [Instalasi](#-instalasi)
- [Struktur Proyek](#-struktur-proyek)
- [Cara Menggunakan](#-cara-menggunakan)
- [Hasil](#-hasil)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Kontributor](#-kontributor)
- [Lisensi](#-lisensi)

## 🎯 Deskripsi

Proyek ini mengimplementasikan model prediksi harga saham untuk 5 saham terbesar di Indonesia:
- **BBCA** - Bank Central Asia
- **TPIA** - Chandra Asri Pacific
- **TLKM** - Telkom Indonesia
- **BRPT** - Barito Pacific
- **ASII** - Astra International

Model menggunakan algoritma XGBoost dengan feature engineering yang mencakup lag features dan moving average untuk meningkatkan akurasi prediksi.

## ✨ Fitur

- ✅ **Eksplorasi Data Lengkap**: Statistik deskriptif, deteksi missing values, dan identifikasi outlier
- ✅ **Feature Engineering**: Pembuatan lag features (5 lags) dan moving average (3 dan 5 periode)
- ✅ **Model Training**: Training XGBoost dengan hyperparameter tuning
- ✅ **Evaluasi Model**: Metrics lengkap (RMSE, MAE, R²) untuk train dan test set
- ✅ **Prediksi Masa Depan**: Prediksi harga 12 minggu ke depan
- ✅ **Visualisasi Komprehensif**: Plot actual vs predicted, feature importance, scatter plot, error distribution, dan forecast plot
- ✅ **Notebook Interaktif**: Jupyter notebook dengan output lengkap di terminal

## 📊 Dataset

Dataset berisi data harga saham mingguan dari 5 perusahaan terbesar di Indonesia. Data mencakup:
- Kolom `Date`: Tanggal pengamatan (format: dd/mm/yyyy)
- Kolom harga saham untuk setiap perusahaan

**File Dataset:**
- `DATA 5 SAHAM TERBESAR TERPERCAYA DAN TERGILA.csv` - Dataset utama

## 🚀 Instalasi

### Prasyarat

- Python 3.7 atau lebih tinggi
- pip (Python package manager)

### Langkah Instalasi

1. **Clone repository ini:**
```bash
git clone https://github.com/username/Machine-Learning-XGBoost.git
cd Machine-Learning-XGBoost
```

2. **Buat virtual environment (disarankan):**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 📁 Struktur Proyek

```
prediksi-harga-saham-xgboost/
│
├── 📄 README.md                          # Dokumentasi utama
├── 📄 requirements.txt                   # Dependencies Python
├── 📄 .gitignore                         # File yang diabaikan Git
├── 📄 LICENSE                            # Lisensi MIT
│
├── 📊 DATA 5 SAHAM TERBESAR TERPERCAYA DAN TERGILA.csv  # Dataset utama
├── 📊 DATA 5 SAHAM FINAL.csv            # Dataset setelah preprocessing
│
├── 📓 Complete_Analysis.ipynb            # Notebook lengkap (Eksplorasi → Visualisasi)
│
├── 🐍 Eksplorasi_Data.py                 # Script eksplorasi data
├── 🐍 Split_Data_Train&Test.py           # Script feature engineering & split data
├── 🐍 Model.py                           # Script training model XGBoost
├── 🐍 Prediksi.py                        # Script prediksi masa depan
├── 🐍 Visualisasi.py                     # Script visualisasi hasil
│
├── 📂 DATA TRAINING DAN TESTING/         # Data train-test split
│   ├── X_train_*.csv
│   ├── X_test_*.csv
│   ├── y_train_*.csv
│   └── y_test_*.csv
│
├── 📂 HASIL XGBOOST/                     # Hasil training model
│   ├── [STOCK]/
│   │   ├── Model_[STOCK].json           # Model yang sudah di-train
│   │   ├── MetricsTrain_[STOCK].csv     # Metrics training
│   │   ├── MetricsTest_[STOCK].csv     # Metrics testing
│   │   ├── PrediksiTrain_[STOCK].csv   # Prediksi training set
│   │   ├── PrediksiTest_[STOCK].csv    # Prediksi test set
│   │   ├── FeatureImportance_[STOCK].csv # Feature importance
│   │   └── Summary_[STOCK].txt          # Ringkasan model
│
├── 📂 HASIL PREDIKSI/                    # Prediksi masa depan
│   ├── [STOCK]_future_12w.csv           # Prediksi 12 minggu
│   └── [STOCK]_future_12w.png            # Plot prediksi
│
└── 📂 HASIL VISUALISASI/                 # Visualisasi hasil
    ├── [STOCK]/
    │   ├── Train_Plot_[STOCK].png
    │   ├── Test_Plot_[STOCK].png
    │   ├── FeatureImportance_[STOCK].png
    │   ├── Scatter_[STOCK].png
    │   └── ErrorHist_[STOCK].png
    ├── Combined_Train_AllStocks.png
    └── Combined_Test_AllStocks.png
```

## 💻 Cara Menggunakan

### Opsi 1: Menggunakan Jupyter Notebook (Disarankan)

1. **Jalankan Jupyter Notebook:**
```bash
jupyter notebook
```

2. **Buka `Complete_Analysis.ipynb`** dan jalankan semua cell secara berurutan

3. **Semua output akan ditampilkan di notebook** (tidak menyimpan file)

### Opsi 2: Menggunakan Script Python

Jalankan script secara berurutan:

```bash
# 1. Eksplorasi Data
python Eksplorasi_Data.py

# 2. Feature Engineering & Split Data
python Split_Data_Train&Test.py

# 3. Training Model
python Model.py

# 4. Prediksi Masa Depan
python Prediksi.py

# 5. Visualisasi
python Visualisasi.py
```

### Parameter Model

Parameter XGBoost yang digunakan:
- `n_estimators`: 300
- `learning_rate`: 0.05
- `max_depth`: 3
- `subsample`: 0.8
- `colsample_bytree`: 0.8
- `reg_lambda`: 2.0
- `min_child_weight`: 3
- `random_state`: 42

### Feature Engineering

- **Lag Features**: 5 lag features (lag1 sampai lag5)
- **Moving Average**: MA3 dan MA5
- **Train-Test Split**: 80% training, 20% testing

## 📈 Hasil

Model menghasilkan metrics evaluasi untuk setiap saham:
- **RMSE** (Root Mean Squared Error)
- **MAE** (Mean Absolute Error)
- **R²** (Coefficient of Determination)

Hasil prediksi dan visualisasi tersimpan di folder:
- `HASIL XGBOOST/` - Model dan metrics
- `HASIL PREDIKSI/` - Prediksi 12 minggu ke depan
- `HASIL VISUALISASI/` - Plot dan grafik

## 🛠️ Teknologi yang Digunakan

- **Python 3.7+**
- **Pandas** - Data manipulation dan analysis
- **NumPy** - Numerical computing
- **XGBoost** - Gradient boosting framework
- **Scikit-learn** - Machine learning metrics
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical data visualization
- **Jupyter Notebook** - Interactive development

## 📝 Catatan

- Dataset yang digunakan adalah data historis harga saham
- Prediksi masa depan menggunakan recursive forecasting
- Model ini untuk tujuan edukasi dan penelitian
- Hasil prediksi tidak menjamin akurasi di dunia nyata

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:
1. Fork repository ini
2. Buat branch untuk fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 Lisensi

Proyek ini menggunakan lisensi MIT. Lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

## 🙏 Acknowledgments

- Dataset: [Sumber dataset jika ada]
- XGBoost: [https://xgboost.readthedocs.io/](https://xgboost.readthedocs.io/)
- Scikit-learn: [https://scikit-learn.org/](https://scikit-learn.org/)

## 📧 Kontak

Untuk pertanyaan atau saran, silakan buat issue di repository ini.

---

⭐ Jika proyek ini membantu, jangan lupa berikan star!




