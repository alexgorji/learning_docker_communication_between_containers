import os
import socket
import subprocess
import threading

HOST = socket.gethostbyname(os.getenv('HOSTNAME'))
PORT = int(os.getenv('SOCKET_PORT'))


def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    # Handle communication with the client
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        if data.decode() == 'create_backup':
            subprocess.call(["sh", "./copy-to-backup.sh"])
            client_socket.sendall(b'demo-2: backup created')
        else:
            client_socket.sendall(b'demo-2 does not understand command ' + data)
    print(f"Connection with {address} closed")
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()


if __name__ == "__main__":
    main()
