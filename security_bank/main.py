from encryption import encrypt_data, decrypt_data
from authentication import authenticate_user
from data_storage import store_data, retrieve_data

def main():
    print("Selamat datang di Sistem Keamanan Data Bank")
    
    if not authenticate_user():
        print("Autentikasi gagal. Program dihentikan.")
        return
    
    while True:
        print("\nMenu:")
        print("1. Simpan Data")
        print("2. Ambil Data")
        print("3. Keluar")
        
        choice = input("Pilih opsi: ")

        if choice == "1":
            data = input("Masukkan data yang ingin disimpan: ")
            encrypted_data = encrypt_data(data)
            store_data(encrypted_data)
            print("Data berhasil disimpan dengan aman.")
        elif choice == "2":
            encrypted_data = retrieve_data()
            if encrypted_data:
                decrypted_data = decrypt_data(encrypted_data)
                print(f"Data yang disimpan: {decrypted_data}")
            else:
                print("Tidak ada data yang ditemukan.")
        elif choice == "3":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
