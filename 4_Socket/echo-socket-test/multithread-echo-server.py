import socket
import threading


def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    # Handle communication with the client
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)  # Echo back the received data

    print(f"Connection with {address} closed")
    client_socket.close()


def main():
    host = '127.0.0.1'
    port = 9991

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()


if __name__ == "__main__":
    main()
