import os

KEY = os.urandom(16)
INITIALIZATION_VECTOR = os.urandom(16) # adds randomness & uniqueness to the encryption process