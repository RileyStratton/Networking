# Echo server program
import socket
import json

# with open("code/ip.json") as infile:
#     ip = json.load(infile)

# NAME = socket.gethostname()

# HOST = ip[NAME]["ip"]
# PORT = ip[NAME]["port"]

HOST = socket.gethostbyname(socket.gethostname())
# HOST = input("Please specify Host IP address (ex. 127.0.0.1): ") 
PORT = 50007

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