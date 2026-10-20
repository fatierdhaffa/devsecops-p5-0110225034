# SecureCalc

## 1. Nama dan Fungsi Aplikasi

SecureCalc adalah aplikasi kalkulator sederhana berbasis Python yang mendukung operasi penjumlahan, pengurangan, perkalian, dan pembagian. Aplikasi ini dilengkapi validasi input dan penanganan kesalahan dasar untuk membantu mengurangi kesalahan saat pengguna memasukkan data atau melakukan perhitungan.

## 2. Bahasa dan Framework

- Bahasa pemrograman: Python
- Unit testing: `unittest`
- Static Application Security Testing (SAST): Bandit
- Otomatisasi pipeline: GitHub Actions

## 3. Cara Menjalankan Aplikasi

Pastikan Python sudah terinstal di komputer.

Jalankan aplikasi melalui terminal:

```bash
python app.py
```

Untuk menjalankan unit test:

```bash
python -m unittest -v
```

Untuk menginstal dependensi dan Bandit:

```bash
python -m pip install -r requirements.txt
```

Untuk menjalankan pemindaian keamanan secara lokal:

```bash
bandit -r app.py calculator.py validator.py formatter.py security_utils.py
```

## 4. Overview Pipeline CI/CD

Proyek SecureCalc menggunakan GitHub Actions untuk menjalankan pipeline secara otomatis ketika terjadi `push` ke branch `main` atau `pull_request` yang menargetkan branch `main`.

Pipeline terdiri dari dua job:

1. **`build`** — menyiapkan lingkungan Python, menginstal dependensi, dan menjalankan unit test untuk memeriksa fungsi aplikasi.
2. **`sast-scan`** — menjalankan Bandit untuk memindai potensi masalah keamanan pada source code Python. Job ini dijalankan setelah job `build` berhasil melalui konfigurasi `needs: build`.

Kedua job menggunakan runner `ubuntu-latest`. Dengan pipeline ini, pengujian dan pemindaian keamanan dapat dilakukan secara otomatis setiap kali perubahan kode dikirim ke repository.
