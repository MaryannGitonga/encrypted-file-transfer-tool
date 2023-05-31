from Crypto.Cipher import AES
import os

key = os.urandom(16)
initialization_vector = os.urandom(16) 

def encrypt(data: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_EAX, initialization_vector)
    ciphertext = cipher.encrypt(b"Hello World!")

    return ciphertext

def decrypt(ciphertext: bytes) -> bytes:
    decipher = AES.new(key, AES.MODE_EAX, initialization_vector)
    plaintext = decipher.decrypt(ciphertext)

    return plaintext
 