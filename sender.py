import os
import socket
from encrypt_decrypt import encrypt

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

file = "test_file"
file_size = os.path.getsize(file)

with open(file, "rb") as f:
    data = f.read()

encrypted = encrypt(data)

client.send((file + ".txt").encode())
client.send(str(file_size).encode())
client.sendall(encrypted)
client.send(b"..END..")

client.close()