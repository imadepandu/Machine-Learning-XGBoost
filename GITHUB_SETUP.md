# 🚀 Panduan Mempublish Proyek ke GitHub

Panduan lengkap untuk mempublish proyek ini ke GitHub.

## 📋 Prasyarat

Sebelum memulai, pastikan Anda sudah menginstal:

1. **Git** - Versi control system
   - Jika belum terinstal, lihat bagian [Instalasi Git](#-instalasi-git) di bawah
   - Verifikasi dengan menjalankan: `git --version`

2. **Akun GitHub** - Buat akun di [github.com](https://github.com) jika belum punya

## 📋 Langkah-langkah

### 1. Buat Repository di GitHub

1. Login ke [GitHub](https://github.com)
2. Klik tombol **"+"** di kanan atas → **"New repository"**
3. Isi informasi:
   - **Repository name**: `prediksi-harga-saham-xgboost` (atau nama lain)
   - **Description**: "Prediksi Harga Saham dengan XGBoost - Machine Learning Project"
   - **Visibility**: Public (atau Private jika ingin private)
   - **JANGAN** centang "Initialize with README" (karena kita sudah punya)
4. Klik **"Create repository"**

### 2. Inisialisasi Git di Proyek Lokal

Buka terminal/command prompt di folder proyek Anda:

```bash
# Inisialisasi Git repository
git init

# Tambahkan semua file ke staging
git add .

# Buat commit pertama
git commit -m "Initial commit: Prediksi Harga Saham dengan XGBoost"
```

### 3. Hubungkan dengan GitHub Repository

```bash
# Tambahkan remote repository (ganti USERNAME dengan username GitHub Anda)
git remote add origin https://github.com/USERNAME/prediksi-harga-saham-xgboost.git

# Atau jika menggunakan SSH:
# git remote add origin git@github.com:USERNAME/prediksi-harga-saham-xgboost.git

# Verifikasi remote sudah ditambahkan
git remote -v
```

### 4. Push ke GitHub

```bash
# Push ke branch main/master
git branch -M main
git push -u origin main
```

Jika menggunakan branch `master`:
```bash
git push -u origin master
```

### 5. Verifikasi

1. Buka repository di browser: `https://github.com/USERNAME/prediksi-harga-saham-xgboost`
2. Pastikan semua file sudah ter-upload
3. README.md seharusnya otomatis tampil di halaman utama

## 🔧 Konfigurasi Tambahan (Opsional)

### Menambahkan Topics/Tags

Di halaman repository GitHub:
1. Klik **⚙️ Settings** → **Topics**
2. Tambahkan tags: `machine-learning`, `xgboost`, `stock-prediction`, `python`, `data-science`

### Menambahkan Description

Di halaman repository:
1. Klik **⚙️ Settings**
2. Scroll ke **"About"**
3. Tambahkan description dan website (jika ada)

### Menambahkan Badges (Opsional)

Tambahkan badges di README.md untuk menampilkan:
- Status build
- License
- Python version
- dll

## 📝 Tips untuk Repository yang Profesional

### 1. **README yang Baik** ✅
- Sudah dibuat dengan lengkap
- Termasuk deskripsi, instalasi, penggunaan
- Ada screenshot/gambar jika perlu

### 2. **.gitignore** ✅
- Sudah dikonfigurasi untuk Python/ML project
- Mencegah commit file yang tidak perlu

### 3. **LICENSE** ✅
- MIT License sudah ditambahkan
- Memberikan izin penggunaan yang jelas

### 4. **requirements.txt** ✅
- Dependencies sudah didokumentasikan
- Memudahkan instalasi

### 5. **CONTRIBUTING.md** ✅
- Panduan untuk kontributor
- Membuat proyek lebih kolaboratif

### 6. **Struktur Folder yang Rapi** ✅
- Folder terorganisir dengan baik
- Nama file konsisten

## 🔄 Update Repository

Setelah melakukan perubahan:

```bash
# Cek status perubahan
git status

# Tambahkan file yang berubah
git add .

# Commit perubahan
git commit -m "Deskripsi perubahan yang jelas"

# Push ke GitHub
git push
```

## 🐛 Troubleshooting

### Error: "git is not recognized" atau "The term 'git' is not recognized"

**Masalah**: Git belum terinstal di Windows Anda.

**Solusi**: Ikuti langkah-langkah di bagian [Instalasi Git](#-instalasi-git) di bawah.

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/USERNAME/prediksi-harga-saham-xgboost.git
```

### Error: "failed to push some refs"
```bash
# Pull dulu perubahan dari GitHub (jika ada)
git pull origin main --allow-unrelated-histories

# Lalu push lagi
git push -u origin main
```

### Error: Authentication failed
- Gunakan Personal Access Token (PAT) sebagai password
- Atau setup SSH key untuk GitHub

## 💻 Instalasi Git (Windows)

Jika Anda mendapat error `git is not recognized`, ikuti langkah berikut:

### Metode 1: Menggunakan Git untuk Windows (Recommended)

1. **Download Git untuk Windows**
   - Kunjungi: https://git-scm.com/download/win
   - Atau langsung: https://github.com/git-for-windows/git/releases/latest
   - Download file installer (misalnya: `Git-2.x.x-64-bit.exe`)

2. **Install Git**
   - Jalankan file installer yang sudah didownload
   - Ikuti wizard instalasi (biasanya klik "Next" untuk semua opsi default)
   - Pilih editor teks favorit Anda (atau biarkan default)
   - Pilih opsi: **"Git from the command line and also from 3rd-party software"** (penting!)
   - Biarkan opsi lainnya default
   - Klik "Install" dan tunggu sampai selesai

3. **Verifikasi Instalasi**
   - Buka PowerShell baru (tutup dan buka lagi)
   - Jalankan: `git --version`
   - Jika muncul versi Git (misalnya: `git version 2.x.x`), berarti berhasil!

4. **Konfigurasi Awal Git (Opsional tapi Recommended)**
   ```bash
   # Set nama Anda
   git config --global user.name "Nama Anda"
   
   # Set email GitHub Anda
   git config --global user.email "email@example.com"
   ```

### Metode 2: Menggunakan Chocolatey (Jika sudah terinstal)

Jika Anda sudah menggunakan Chocolatey, bisa install dengan:
```powershell
choco install git
```

### Metode 3: Menggunakan Winget (Windows 10/11)

```powershell
winget install --id Git.Git -e --source winget
```

### Setelah Instalasi

1. **Restart Terminal/PowerShell** (penting!)
   - Tutup semua jendela PowerShell/CMD yang terbuka
   - Buka terminal baru

2. **Cek Git sudah berfungsi**
   ```bash
   git --version
   ```

3. **Lanjutkan ke Tahap 2** dari panduan utama

### Troubleshooting Instalasi Git

- **Git masih tidak dikenali setelah instalasi?**
  - Tutup semua jendela terminal dan buka yang baru
  - Restart komputer (kadang diperlukan)
  - Cek di Settings → System → About → Advanced system settings → Environment Variables
    - Pastikan `C:\Program Files\Git\cmd` ada di PATH

- **Butuh bantuan lebih lanjut?**
  - Dokumentasi resmi: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

## 📚 Resources

- [GitHub Docs](https://docs.github.com/)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [GitHub Guides](https://guides.github.com/)

## ✅ Checklist Sebelum Push

- [ ] README.md sudah lengkap dan informatif
- [ ] .gitignore sudah dikonfigurasi
- [ ] requirements.txt sudah ada
- [ ] LICENSE sudah ditambahkan
- [ ] Kode sudah di-test dan berjalan
- [ ] Tidak ada file sensitif (API keys, passwords, dll)
- [ ] Commit message jelas dan deskriptif

---

**Selamat! Proyek Anda sudah siap dipublish ke GitHub! 🎉**




