# Echo client program
import socket
import json

with open("code/ip.json") as infile:
    ip = json.load(infile)

HOST = ip["desktop"]["ip"]                # The remote host
PORT = ip["desktop"]["port"]              # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = input("Message: ")
    s.sendall(msg.encode())
#     data = s.recv(1024)
# print('Received', repr(data))