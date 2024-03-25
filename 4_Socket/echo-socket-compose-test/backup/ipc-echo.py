import socket
import sys

HOST = socket.gethostbyname(sys.argv[1])
PORT = int(sys.argv[2])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello world. IPC success!')
    data = s.recv(1024)

print(f"Received {data!r}")
