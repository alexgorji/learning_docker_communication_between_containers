import socket
import sys

HOST = socket.gethostbyname(sys.argv[1])
PORT = int(sys.argv[2])
COMMAND = str.encode(sys.argv[3])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(COMMAND)
    data = s.recv(1024)

print(f"Received {data!r}")
