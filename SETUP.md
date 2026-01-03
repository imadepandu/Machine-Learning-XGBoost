# Panduan Setup Proyek

Panduan lengkap untuk setup dan menjalankan proyek ini.

## Prasyarat

- Python 3.7 atau lebih tinggi
- pip (Python package manager)
- Git (untuk clone repository)

## Langkah-langkah Setup

### 1. Clone Repository

```bash
git clone https://github.com/username/prediksi-harga-saham-xgboost.git
cd prediksi-harga-saham-xgboost
```

### 2. Buat Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verifikasi Instalasi

```bash
python -c "import pandas, numpy, xgboost, sklearn, matplotlib, seaborn; print('All packages installed successfully!')"
```

### 5. Jalankan Proyek

**Opsi A: Menggunakan Jupyter Notebook (Disarankan)**
```bash
jupyter notebook
```
Buka `Complete_Analysis.ipynb` dan jalankan semua cell.

**Opsi B: Menggunakan Script Python**
```bash
python Eksplorasi_Data.py
python Split_Data_Train&Test.py
python Model.py
python Prediksi.py
python Visualisasi.py
```

## Troubleshooting

### Error: ModuleNotFoundError
- Pastikan virtual environment sudah diaktifkan
- Install ulang dependencies: `pip install -r requirements.txt`

### Error: FileNotFoundError
- Pastikan file dataset ada di folder root
- Periksa nama file dataset sesuai dengan yang ada di kode

### Error: Memory Error
- Kurangi ukuran dataset atau gunakan subset data
- Tutup aplikasi lain yang menggunakan banyak memori

## Struktur Folder yang Akan Dibuat

Setelah menjalankan script, folder berikut akan dibuat otomatis:
- `DATA TRAINING DAN TESTING/` - Data train-test split
- `HASIL XGBOOST/` - Model dan metrics
- `HASIL PREDIKSI/` - Prediksi masa depan
- `HASIL VISUALISASI/` - Plot dan grafik

## Catatan

- Pastikan ada ruang disk yang cukup untuk menyimpan hasil
- Waktu eksekusi tergantung pada ukuran dataset dan spesifikasi komputer
- Untuk dataset besar, proses training mungkin memakan waktu lama




