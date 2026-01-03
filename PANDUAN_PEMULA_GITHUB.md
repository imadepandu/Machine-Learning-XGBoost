# 🎯 Panduan Sederhana Publish ke GitHub untuk Pemula

Panduan step-by-step yang sangat mudah diikuti untuk yang pertama kali publish ke GitHub.

---

## ✅ LANGKAH 1: Persiapan - Install Git

### Apakah Git sudah terinstall?

Buka PowerShell dan ketik:
```powershell
git --version
```

**Jika muncul error atau "not recognized":**
- Git belum terinstall
- Ikuti langkah install di bawah

**Jika muncul versi (misal: `git version 2.43.0`):**
- Git sudah terinstall ✅
- Langsung ke LANGKAH 2

---

### Cara Install Git (Jika Belum Ada)

1. **Buka browser, kunjungi:**
   ```
   https://git-scm.com/download/win
   ```
   Atau langsung: https://github.com/git-for-windows/git/releases/latest

2. **Download file installer**
   - Klik file yang namanya seperti: `Git-2.43.0-64-bit.exe`
   - Tunggu download selesai

3. **Jalankan installer**
   - Double-click file yang sudah didownload
   - Klik **"Next"** terus sampai muncul pilihan editor
   - Pilih editor (bisa pilih default atau Notepad++)
   - Di halaman "Adjusting your PATH environment":
     - **PILIH**: "Git from the command line and also from 3rd-party software"
     - Ini penting! ✅
   - Klik **"Next"** terus, lalu **"Install"**
   - Tunggu sampai selesai

4. **Restart PowerShell**
   - **Tutup semua PowerShell** yang terbuka
   - Buka PowerShell baru
   - Ketik lagi: `git --version`
   - Harusnya sekarang muncul versi Git ✅

5. **Setup Nama dan Email (Penting!)**
   ```powershell
   git config --global user.name "Nama Anda"
   git config --global user.email "email@example.com"
   ```
   **Contoh:**
   ```powershell
   git config --global user.name "imadepandu"
   git config --global user.email "imadepandu@gmail.com"
   ```
   **Ganti dengan nama dan email Anda!**

---

## ✅ LANGKAH 2: Pastikan Anda di Folder Proyek yang Benar

1. **Buka PowerShell**

2. **Masuk ke folder proyek Anda**
   ```powershell
   cd "E:\imadepandu\SEMESTER 5\Model Prediction and Machine Learning\UAS_Machine Learning_Kelompok 4"
   ```

3. **Pastikan Anda di folder yang benar**
   ```powershell
   pwd
   ```
   Harusnya muncul: `E:\imadepandu\SEMESTER 5\Model Prediction and Machine Learning\UAS_Machine Learning_Kelompok 4`

4. **Cek file-file proyek ada**
   ```powershell
   dir
   ```
   Harusnya muncul file seperti: `README.md`, `requirements.txt`, dll

---

## ✅ LANGKAH 3: Buat Repository di GitHub (Website)

**JANGAN** lanjut ke langkah ini kalau Git belum terinstall!

1. **Buka browser, login ke GitHub**
   - Kunjungi: https://github.com
   - Login dengan akun Anda (atau buat akun baru dulu)

2. **Buat Repository Baru**
   - Klik tombol **"+"** di pojok kanan atas
   - Pilih **"New repository"**

3. **Isi Form:**
   - **Repository name**: `prediksi-harga-saham-xgboost`
     (bisa pakai nama lain, tapi jangan pakai spasi)
   - **Description**: `Prediksi Harga Saham dengan XGBoost - Machine Learning Project`
   - **Public** atau **Private**? Pilih salah satu (Public lebih umum)
   - **JANGAN CENTANG** "Add a README file"
   - **JANGAN CENTANG** "Add .gitignore"
   - **JANGAN CENTANG** "Choose a license"
   
   Kita sudah punya file-file ini!

4. **Klik "Create repository"**

5. **Copy URL Repository**
   - Setelah repository dibuat, akan muncul halaman dengan instruksi
   - Ada URL yang bentuknya: `https://github.com/USERNAME/prediksi-harga-saham-xgboost.git`
   - **COPY URL INI** (ganti USERNAME dengan username GitHub Anda)
   - Contoh: `https://github.com/imadepandu/prediksi-harga-saham-xgboost.git`
   - Simpan URL ini, akan dipakai nanti!

---

## ✅ LANGKAH 4: Setup Git di Komputer (Lokal)

**Kembali ke PowerShell di folder proyek Anda!**

### 4.1. Inisialisasi Git Repository
```powershell
git init
```
**Output yang benar:**
```
Initialized empty Git repository in E:/imadepandu/SEMESTER 5/Model Prediction and Machine Learning/UAS_Machine Learning_Kelompok 4/.git/
```

⚠️ **Jika muncul path yang berbeda** (misal `C:/Users/...`), berarti Anda tidak di folder proyek yang benar. Ulangi LANGKAH 2!

### 4.2. Tambahkan Semua File ke Git
```powershell
git add .
```
Ini akan menambahkan semua file ke "staging area". Tidak ada output biasanya.

### 4.3. Buat Commit Pertama
```powershell
git commit -m "Initial commit: Prediksi Harga Saham dengan XGBoost"
```
**Output yang benar:**
```
[main (or master) xxxxxxx] Initial commit: Prediksi Harga Saham dengan XGBoost
 X files changed, X insertions(+)
```

---

## ✅ LANGKAH 5: Hubungkan dengan GitHub

### 5.1. Tambahkan Remote Repository

**Ganti USERNAME dengan username GitHub Anda!**

```powershell
git remote add origin https://github.com/USERNAME/prediksi-harga-saham-xgboost.git
```

**Contoh:**
```powershell
git remote add origin https://github.com/imadepandu/prediksi-harga-saham-xgboost.git
```

### 5.2. Verifikasi Remote Sudah Ditambahkan
```powershell
git remote -v
```

**Output yang benar:**
```
origin  https://github.com/USERNAME/prediksi-harga-saham-xgboost.git (fetch)
origin  https://github.com/USERNAME/prediksi-harga-saham-xgboost.git (push)
```

---

## ✅ LANGKAH 6: Push ke GitHub

### 6.1. Set Branch ke "main"
```powershell
git branch -M main
```

### 6.2. Push ke GitHub
```powershell
git push -u origin main
```

### 6.3. Login Authentication

**Jika diminta login:**
- **Username**: Masukkan username GitHub Anda
- **Password**: JANGAN pakai password GitHub biasa!
  - Gunakan **Personal Access Token (PAT)**
  - Cara buat PAT ada di LANGKAH 7 di bawah

**Jika berhasil, output:**
```
Enumerating objects: XX, done.
Counting objects: 100% (XX/XX), done.
Writing objects: 100% (XX/XX), done.
To https://github.com/USERNAME/prediksi-harga-saham-xgboost.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

🎉 **SELESAI!** File Anda sudah di GitHub!

---

## ✅ LANGKAH 7: Buat Personal Access Token (Jika Diperlukan)

Jika saat push diminta password dan password biasa tidak bekerja:

1. **Buka GitHub Settings**
   - Login ke GitHub
   - Klik foto profil (pojok kanan atas)
   - Pilih **"Settings"**

2. **Buat Token**
   - Scroll ke bawah, klik **"Developer settings"** (di menu kiri bawah)
   - Klik **"Personal access tokens"**
   - Klik **"Tokens (classic)"**
   - Klik **"Generate new token"**
   - Pilih **"Generate new token (classic)"**

3. **Isi Form:**
   - **Note**: `Untuk push dari komputer`
   - **Expiration**: Pilih berapa lama (misal 90 days)
   - **Scopes**: Centang **"repo"** (akan centang semua yang ada di bawahnya)
   - Scroll ke bawah, klik **"Generate token"**

4. **Copy Token**
   - **PENTING!** Token hanya muncul sekali!
   - **Copy token ini** dan simpan dengan aman
   - Token bentuknya seperti: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

5. **Gunakan Token sebagai Password**
   - Saat push dan diminta password
   - Paste token ini (bukan password GitHub Anda)

---

## ✅ LANGKAH 8: Verifikasi

1. **Buka repository di browser:**
   ```
   https://github.com/USERNAME/prediksi-harga-saham-xgboost
   ```
   (Ganti USERNAME dengan username Anda)

2. **Cek:**
   - ✅ Semua file sudah ada
   - ✅ README.md tampil di halaman utama
   - ✅ Folder `.git` TIDAK muncul (normal, karena di .gitignore)

---

## 🐛 Troubleshooting

### Error: "git is not recognized"
→ Git belum terinstall. Kembali ke LANGKAH 1.

### Error: "Initialized empty Git repository in C:/Users/..."
→ Anda tidak di folder proyek yang benar. Kembali ke LANGKAH 2.

### Error: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/USERNAME/prediksi-harga-saham-xgboost.git
```

### Error: "Authentication failed"
→ Gunakan Personal Access Token (LANGKAH 7), bukan password GitHub.

### Error: "failed to push some refs"
```powershell
git pull origin main --allow-unrelated-histories
git push -u origin main
```

---

## 📝 Checklist Sebelum Push

- [ ] Git sudah terinstall dan bisa jalan
- [ ] Sudah setup nama dan email di Git
- [ ] Sudah di folder proyek yang benar
- [ ] Repository di GitHub sudah dibuat
- [ ] Sudah copy URL repository
- [ ] Sudah buat Personal Access Token (jika diperlukan)

---

## 🎉 Selamat!

Proyek Anda sudah berhasil dipublish ke GitHub!

**Tips:**
- Setiap kali ada perubahan, ulangi:
  ```powershell
  git add .
  git commit -m "Deskripsi perubahan"
  git push
  ```

- Jangan lupa update README.md jika ada perubahan penting!

---

**Butuh bantuan?** Cek file `GITHUB_SETUP.md` untuk panduan lebih detail!

