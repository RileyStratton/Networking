# Echo server program
import socket
import json

with open("code/ip.json") as infile:
    ip = json.load(infile)

NAME = socket.gethostname()

HOST = ip[NAME]["ip"]                 # Symbolic name meaning all available interfaces
PORT = ip[NAME]["port"]               # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    print(f"Server started on {HOST}:{PORT}")

    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print(f"Client connected from {addr[0]}:{addr[1]}")
        while True:
            msg = conn.recv(1024).decode()
            if msg != "":
                print(msg)

                
            # if not data: break
            # conn.sendall(data)