import socket
import threading
import os

HOST = socket.gethostbyname(os.getenv('HOSTNAME'))
PORT = int(os.getenv('SOCKET_PORT'))


def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    # Handle communication with the client
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(b'data received: ' + data)
        echo = b'Echo from demo-2: ' + data
        client_socket.sendall(echo)  # Echo back the received data

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
