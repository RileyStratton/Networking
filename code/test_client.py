# Echo client program
import socket

HOST = '192.168.86.24'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = input("Message: ")
    s.sendall(msg.encode())
#     data = s.recv(1024)
# print('Received', repr(data))