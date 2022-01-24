import json
import socket

from connection_gui import ConnectionGUI
from messages import Messages

class Connection():
    def __init__(self):
        self.connection_gui = ConnectionGUI()
        self.session_type = self.connection_gui.input_session_type()
        self.session_addr = self.connection_gui.input_session_ip_port()
        self.ip = self.session_addr[0]
        self.port = self.session_addr[1]

        if self.session_type == "start": 
            self.peer_start()
        elif self.session_type == "connect": 
            self.peer_connect()

    def peer_start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as unconnected_sock:
            unconnected_sock.bind((self.ip, self.port))

            print(f"Session started at {self.ip}:{self.port}")

            unconnected_sock.listen(1)
            
            self.sock, self.addr = unconnected_sock.accept()
            with self.sock:
                self.save_addresses()
                
                self.messages = Messages(self.sock)

                # Beta Test
                # while True:
                #     msg = self.conn.recv(1024).decode()
                #     if msg != "":
                #         print(msg)

    def peer_connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            self.sock.connect((self.ip, self.port))
            self.save_addresses()

            self.messages = Messages(self.sock)

            # Beta Test
            # print("Type your message and hit enter to send it to the host!")
            # while True:
            #     msg = input("")
            #     self.sock.sendall(msg.encode())

    def save_addresses(self):
        addr_self = self.sock.getsockname()
        addr_peer = self.sock.getpeername()

        with open("code/addresses.json", "r") as infile:
            addresses = json.load(infile)

        addresses["previous_self"]={
            "ip":addr_self[0],
            "port":addr_self[1]}

        addresses["previous_peer"]={
            "ip":addr_peer[0],
            "port":addr_peer[1]}

        with open("code/addresses.json", "w") as outfile:
            json.dump(addresses, outfile, indent=4)