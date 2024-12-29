# Security Bank

Proyek ini adalah aplikasi Python yang dirancang untuk menjaga keamanan dan privasi data pengguna, seperti data bank. Aplikasi ini mencakup fitur enkripsi dan dekripsi data, autentikasi pengguna, serta penyimpanan data yang aman.

## Fitur

- **Autentikasi pengguna**: Memastikan hanya pengguna yang terautentikasi yang bisa mengakses aplikasi.
- **Enkripsi data**: Data yang disimpan akan dienkripsi dengan kunci khusus menggunakan algoritma kriptografi.
- **Penyimpanan data**: Data terenkripsi disimpan ke dalam file dan dapat diambil serta didekripsi.

## Instalasi

1. Clone repositori ini atau buat folder proyek dengan struktur yang sesuai.
   
2. Masuk ke direktori proyek menggunakan terminal atau command prompt:
   ```bash
   cd path/to/data_bank_security_project

## Hasil Output

```yaml
Selamat datang di Sistem Keamanan Data Bank

Masukkan username: admin
Masukkan password: ********
Autentikasi berhasil!

Menu:
1. Simpan Data
2. Ambil Data
3. Keluar

Pilih opsi: 1
Masukkan data yang ingin disimpan: Data yang ingin disimpan di dalam bank
Data berhasil disimpan dengan aman.

Menu:
1. Simpan Data
2. Ambil Data
3. Keluar

Pilih opsi: 2
Data yang disimpan: Data yang ingin disimpan di dalam bank

Terima kasih. Program selesai.

(data_encrypted:
  - "gAAAAABlYgfO7U8sZ0xv2Vf3zJqKZhbT6IvmG2D04wfh6QkFhZ5kU42sn3q6J89XmRH-7cZXy7m4bn4hwvDHFpUwJjt5-2Tj0A=="

data_decrypted:
  - "Data yang ingin disimpan di dalam bank"

authentication:
  status: "success"
  username: "admin"

log:
  - action: "Data disimpan"
    timestamp: "2024-12-29T14:02:15"
  - action: "Data diambil dan didekripsi"
    timestamp: "2024-12-29T14:05:30")

