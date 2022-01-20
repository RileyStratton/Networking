# Echo server program
import socket
import json

with open("code/ip.json") as infile:
    ip = json.load(infile)

HOST = ip["desktop"]["ip"]                 # Symbolic name meaning all available interfaces
PORT = ip["desktop"]["port"]               # Arbitrary non-privileged port

print(HOST + ":" + PORT)

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
            if msg != "":
                print(msg)

                
            # if not data: break
            # conn.sendall(data)