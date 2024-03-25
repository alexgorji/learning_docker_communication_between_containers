import socket

HOST = "127.0.0.1"  # Standard loopback [The loopback address, also called localhost: an internal address that routes back to the local system. The loopback address in IPv4 is 127.0. 01.] interface address
PORT = 9991  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by", {addr})
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

# Constant AF_INET is the Internet address family for IPv4.
# Constant SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network.
# The .bind() method expects a two-tuple: (host, port) if you’re using socket.AF_INET (IPv4).
# The host can be a hostname, IP address, or empty string [= the server will accept connections on all available IPv4 interfaces.]
# TCP port: 1..65535. Some systems may require superuser privileges if the port number is less than 1024.
# For deterministic behavior use a numeric address in host portion.
# The .listen() method has a backlog parameter. It specifies the number of unaccepted connections that the system will allow before refusing new connections.
# The .accept() method blocks execution and waits for an incoming connection.
# When a client connects, it returns a new socket object representing the connection and a tuple holding the address of the client. The tuple will contain (host, port) for IPv4 connections or (host, port, flowinfo, scopeid) for IPv6.
# Now you have a new socket object from .accept() = conn. It’s the socket that you’ll use to communicate with the client. It’s distinct from the listening socket that the server is using to accept new connections.
# After .accept() provides the client socket object conn, an infinite while loop is used to loop over blocking calls to conn.recv(). This reads whatever data the client sends and echoes it back using conn.sendall().
# A socket function or method that temporarily suspends your application is a blocking call. For example, .accept(), .connect(), .send(), and .recv() block, meaning they don’t return immediately. Blocking calls have to wait on system calls (I/O) to complete before they can return a value. So you, the caller, are blocked until they’re done or a timeout or other error occurs.
# If conn.recv() returns an empty bytes object, b'', that signals that the client closed the connection and the loop is terminated.
# 1024 is the buffer size. Our socket is going to attempt to receive data, in a buffer size of 1024 bytes at a time.
