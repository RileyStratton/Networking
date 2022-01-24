import socket
import json

from connection_gui import ConnectionGUI

class Connection():
    def __init__(self):
        self.connection_gui = ConnectionGUI()
        connection_type = self.connection_gui.input_connection_type()
        self.connection_gui.input_connection_ip_port(connection_type)


    def peer_start(self):
        HOST = socket.gethostbyname(socket.gethostname())
        # HOST = input("Please specify Host IP address (ex. 127.0.0.1): ") 
        PORT = 50007

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            self.sock.bind((HOST, PORT))

            print(f"Server started on {HOST}:{PORT}")

            self.sock.listen(1)
            self.conn, self.addr = self.sock.accept()
            with self.conn:
                self.save_addresses(self.sock)
                print(f"Client connected from {self.addr[0]}:{self.addr[1]}")
                while True:
                    msg = self.conn.recv(1024).decode()
                    if msg != "":
                        print(msg)

    def peer_connect(self):
        HOST = input("Please specify Host IP address (ex. 127.0.0.1): ")     # The remote host
        # PORT = int(input("Please specify Host port (ex. 50007): "))
        PORT = 50007

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            self.sock.connect((HOST, PORT))
            self.save_addresses()

            print("Type your message and hit enter to send it to the host!")
            while True:
                msg = input("")
                self.sock.sendall(msg.encode())

    def save_addresses(self):
        self_address = self.sock.getsockname()
        peer_address = self.sock.getpeername()

        with open("code/addresses.json", "+") as infile:
            addresses = json.load(infile)

            addresses["previous_self"()]={
                "ip":self_address[0],
                "port":self_address[1]}

            addresses["previous_peer"()]={
                "ip":peer_address[0],
                "port":peer_address[1]}

            json.dump(addresses, infile, indent=4)

    def get_previous_address(self, self_or_peer):
        pass