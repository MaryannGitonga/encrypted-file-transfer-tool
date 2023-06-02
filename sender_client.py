from encrypt_decrypt import encrypt
import socket
import os

def send_file(filename: str, server_address: tuple) -> None:
    # Client with an internet socket using connection oriented protocol (TCP)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_address)

    # Send the filename & file size to the server
    encoded_filename_size = (filename + ", " + str(os.path.getsize(filename))).encode()
    client.send(encrypt(encoded_filename_size))

    # Read and send the file data in chunks
    with open(filename, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client.send(encrypt(data))

    client.close()
    print('File sent:', filename)

if __name__ == '__main__':
    server_address = ('localhost', 50000)
    filename = 'test_file.txt'
    send_file(filename, server_address)
