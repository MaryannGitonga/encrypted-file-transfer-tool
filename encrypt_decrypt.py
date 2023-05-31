from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

key = os.urandom(16)
initialization_vector = os.urandom(16) # adds randomness & uniqueness to the encryption process

def encrypt(data: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, initialization_vector)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    return ciphertext

# NB: 
# Once a cipher object has been used for encryption the encryption process alters the internal state of the cipher, 
# and decryption requires the cipher to be in the correct state to perform the reverse transformation.

# Create a new cipher object with the same parameters as used during encryption to ensures that the cipher is properly initialized
def decrypt(ciphertext: bytes) -> bytes:
    decipher = AES.new(key, AES.MODE_EAX, initialization_vector)
    plaintext = decipher.decrypt(unpad(ciphertext, AES.block_size))

    return plaintext
 