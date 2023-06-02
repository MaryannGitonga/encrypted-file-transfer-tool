from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from keys import KEY, INITIALIZATION_VECTOR

def encrypt(data: bytes) -> bytes:
    cipher = AES.new(KEY, AES.MODE_CBC, INITIALIZATION_VECTOR)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return ciphertext

# NB: 
# Once a cipher object has been used for encryption the encryption process alters the internal state of the cipher, 
# and decryption requires the cipher to be in the correct state to perform the reverse transformation.

# Create a new cipher object with the same parameters as used during encryption to ensures that the cipher is properly initialized
def decrypt(ciphertext: bytes) -> bytes:
    decipher = AES.new(KEY, AES.MODE_CBC, INITIALIZATION_VECTOR)
    plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

    return plaintext
 