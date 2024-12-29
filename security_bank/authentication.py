import getpass
def authenticate_user():
    stored_username = "admin"
    stored_password = "password123"
    
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")

    if username == stored_username and password == stored_password:
        return True
    else:
        return False
