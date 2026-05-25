from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key):
        self.key = key
        self.cipher = Fernet(key)

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()
