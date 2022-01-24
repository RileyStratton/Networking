# Echo client program
import socket
import json

def save_address(socket, self_or_peer):
    if self_or_peer.lower() == "self": addr = socket.getsockname()
    elif self_or_peer.lower() == "peer": addr = socket.getpeername()

    with open("code/ip.json", "+") as infile:
        ip = json.load(infile)

        ip["previous_"+self_or_peer.lower()]={
            "ip":addr[0],
            "port":addr[1]}

        json.dump(ip, infile, indent=4)


HOST = input("Please specify Host IP address (ex. 127.0.0.1): ")     # The remote host
# PORT = int(input("Please specify Host port (ex. 50007): "))
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # save_address(s, "peer")
    print("Type your message and hit enter to send it to the host!")
    while True:
        msg = input("")
        s.sendall(msg.encode())
#     data = s.recv(1024)
# print('Received', repr(data))

