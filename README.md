# Security Bank

Aplikasi Python sederhana yang dirancang untuk menjaga keamanan dan privasi data pengguna, seperti data bank.
Aplikasi ini mencakup fitur enkripsi dan dekripsi data, autentikasi pengguna, serta penyimpanan data.

## Fitur

- **Autentikasi pengguna**
- **Enkripsi data**
- **Penyimpanan data**

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

