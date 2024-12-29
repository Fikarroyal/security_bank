import os
def store_data(data):
    with open("data_encrypted.txt", "wb") as file:
        file.write(data)

def retrieve_data():
    if os.path.exists("data_encrypted.txt"):
        with open("data_encrypted.txt", "rb") as file:
            return file.read()
    else:
        print("Tidak ada data yang ditemukan.")
        return None
