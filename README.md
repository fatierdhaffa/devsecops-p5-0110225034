
# SecureCalc

## 1. Nama dan Fungsi Aplikasi

SecureCalc adalah aplikasi kalkulator sederhana berbasis Python yang mendukung operasi penjumlahan, pengurangan, perkalian, dan pembagian. Aplikasi ini menerapkan validasi input dan penanganan kesalahan dasar.

## 2. Bahasa dan Framework

- Bahasa pemrograman: Python
- Unit testing: unittest
- Static Application Security Testing (SAST): Bandit
- CI/CD: GitHub Actions

## 3. Cara Menjalankan Aplikasi

Pastikan Python sudah terinstal.

Jalankan aplikasi melalui terminal:

```bash
python app.py
```

Untuk menjalankan unit test:

```bash
python -m unittest -v
```

Untuk menginstal Bandit secara lokal:

```bash
python -m pip install -r requirements.txt
```

Untuk menjalankan pemindaian keamanan:

```bash
bandit -r . -x ./venv,./.venv
```

## 4. Overview Pipeline CI/CD

Proyek ini menggunakan GitHub Actions untuk menjalankan pipeline secara otomatis ketika terjadi push ke branch `main` atau pull request yang menargetkan branch `main`.

Pipeline terdiri dari dua job:

1. `build`: menyiapkan Python, menginstal dependensi, dan menjalankan unit test.
2. `sast-scan`: menjalankan Bandit untuk memeriksa potensi masalah keamanan pada source code. Job ini dijalankan setelah job `build` berhasil melalui konfigurasi `needs: build`.

Kedua job menggunakan runner `ubuntu-latest`.
