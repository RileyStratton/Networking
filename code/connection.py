import json
import socket

from connection_gui import ConnectionGUI
from messages import Messages

class Connection():
    def __init__(self):
        # Starts up a GUI to collect session type, port, IP address, and username
        self.connection_gui = ConnectionGUI()
        self.session_type = self.connection_gui.input_session_type()
        self.session_addr = self.connection_gui.input_session_ip_port()

        # Stores the collected information to be used
        self.ip = self.session_addr[0]
        self.port = self.session_addr[1]
        self.username = self.session_addr[2]

        # Calls the correct function depending on if the user is starting or connecting
        if self.session_type == "start": 
            self.peer_start()
        elif self.session_type == "connect": 
            self.peer_connect()

    def peer_start(self):
        # Create a socket to be connected to
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as unconnected_sock:
            unconnected_sock.bind((self.ip, self.port))

            # Commented out code
            # print(f"Session started on {self.ip}:{self.port}.\nWaiting for peer to connect.")

            # Listsens for a connection
            unconnected_sock.listen(1)
            self.sock, self.addr = unconnected_sock.accept()
            with self.sock:
                # Saves the connection to be used again (saved file isn't saved to GitHub)
                self.save_addresses()

                # Sends the socket to the messages initialization, and the rest runs from there
                self.messages = Messages(self.sock, self.username)

                # Beta Test
                # while True:
                #     msg = self.conn.recv(1024).decode()
                #     if msg != "":
                #         print(msg)

    def peer_connect(self):
        # Uses the saved info to connect to another peer
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            self.sock.connect((self.ip, self.port))

            # Saves the connection to be used again (saved file isn't saved to GitHub)
            self.save_addresses()

            ## Sends the socket to the messages initialization, and the rest runs from there
            self.messages = Messages(self.sock, self.username)

            # Beta Test
            # print("Type your message and hit enter to send it to the host!")
            # while True:
            #     msg = input("")
            #     self.sock.sendall(msg.encode())

    def save_addresses(self):
        # Retrieves self and peer addresses from the socket
        addr_self = self.sock.getsockname()
        addr_peer = self.sock.getpeername()

        # Opens the a json file and stores it as a dictionary
        try:
            with open("code/addresses.json", "r") as infile:
                addresses = json.load(infile)
        
        # If it doesn't exist, it will create a new dictionary
        except:
            addresses = {}

        # Add self info to dictionary
        addresses["previous_self"]={
            "ip":addr_self[0],
            "port":addr_self[1]}

        # Add peer info to dictionary
        addresses["previous_peer"]={
            "ip":addr_peer[0],
            "port":addr_peer[1]}
        
        # Writes info to a .json file (or creates a new .json file)
        with open("code/addresses.json", "w") as outfile:
            json.dump(addresses, outfile, indent=4)