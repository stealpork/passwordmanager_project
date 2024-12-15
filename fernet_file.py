

from cryptography.fernet import Fernet



cipher = Fernet(b'9CRKYMf_dvgXBF8exr-2z0iDY_G_BEN90u5avPdPeOQ=')

def encrypt(message):
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt(encrypted_message):
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

