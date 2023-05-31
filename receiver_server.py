import socket, os
from encrypt_decrypt import decrypt

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 50000))
    server.listen(1)
    print('Server listening on localhost:50000')

    while True:
        client, address = server.accept()
        print('Client connected:', address)

        # Receive the filename and file size from the client
        filename_size = decrypt(client.recv(1024).decode())

        filename, file_size = filename_size.split(", ")[0], filename_size.split(", ")[1]

        print('Received file:', filename)

        # Open the file and write the data received from the client
        with open(os.path.splitext(filename)[0] + "_sent" + os.path.splitext(filename)[1], 'wb') as file:
            total_received = 0
            while total_received < int(file_size):
                data = client.recv(1024)
                file.write(decrypt(data))
                total_received += len(data)

        print('File saved:', filename)
        client.close()

if __name__ == '__main__':
    main()
