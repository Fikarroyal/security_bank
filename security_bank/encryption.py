from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(data):
    key = generate_key()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    key = generate_key()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data
