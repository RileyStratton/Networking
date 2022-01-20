# Echo client program
import socket

HOST = input("Please specify server IP address (ex. 127.0.0.1): ")                # The remote host
PORT = int(input("Please specify server port (ex. 50007): "))             # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input("Message: ")
        s.sendall(msg.encode())
#     data = s.recv(1024)
# print('Received', repr(data))