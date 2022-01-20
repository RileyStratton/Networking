# Echo server program
import socket

HOST = '192.168.86.24'                 # Symbolic name meaning all available interfaces
PORT = 50007                           # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    print(f"Server started on {HOST}:{PORT}")
    print(f"Waiting for clients...")

    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            msg = conn.recv(1024).decode()
            print(msg)
            # if not data: break
            # conn.sendall(data)