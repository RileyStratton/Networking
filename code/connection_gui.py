import re
import json
import socket

from tkinter import *
from tkinter import ttk

class ConnectionGUI():

    def input_session_type(self):
        self.screen = Tk()
        self.screen.title("Session Type")
        self.frame = ttk.Frame(self.screen, padding=10)
        self.frame.grid()

        self.start_button = ttk.Button(self.frame, text="START", command=lambda:self.submit_session_type("start"))
        self.start_button.grid(column=0, row=0)
        self.start_instructions = ttk.Label(self.frame, text="Start a session that a \npeer can connect to.")
        self.start_instructions.grid(column=0, row=1, padx=10)

        self.connect_button = ttk.Button(self.frame, text="CONNECT", command=lambda: self.submit_session_type("connect"))
        self.connect_button.grid(column=1, row=0)
        self.connect_instructions = ttk.Label(self.frame, text="Connect to a peer that \nhas started a session." )
        self.connect_instructions.grid(column=1, row=1, padx=10)

        self.screen.mainloop()
        return self.session_type

    def submit_session_type(self, type):
        self.session_type = type

        self.screen.destroy()

    def input_session_ip_port(self):
        self.screen = Tk()
        self.screen.title("Session Address")
        self.frame = ttk.Frame(self.screen, padding=10)
        self.frame.grid()

        if self.session_type == "start":
            self.intro_label = ttk.Label(self.frame, text="Enter your device's IP address and desired port (default is 50007).")
        elif self.session_type == "connect":
            self.intro_label = ttk.Label(self.frame, text="Enter the IP address and port (default is 50007) of the peer device you are trying to connect to.")
        self.intro_label.grid(column=0, row=0, columnspan=2)

        self.username_info = ttk.Label(self.frame, text="If you would like to hide your IP address, please enter a username.")
        self.username_info.grid(column=0, row=1, columnspan=2)

        self.autofill_label = ttk.Label(self.frame, text="Autofill will attempt to autofill your device's IP addres, but verify it for accuracy.")
        self.autofill_label.grid(column=0, row=2, columnspan=2)

        self.previous_label = ttk.Label(self.frame, text="You can also use a previous entry if you have connected before.")
        self.previous_label.grid(column=0, row=3, columnspan=2)

        self.ip_label = ttk.Label(self.frame, text="IP: ")
        self.ip_label.grid(column=0, row=4, sticky="e")
        self.ip_entry = ttk.Entry(self.frame)
        self.ip_entry.grid(column=1, row=4, sticky="w")
        self.ip_entry.insert(0, "127.0.0.1")

        self.port_label = ttk.Label(self.frame, text="Port: ")
        self.port_label.grid(column=0, row=5, sticky="e")
        self.port_entry = ttk.Entry(self.frame)
        self.port_entry.grid(column=1, row=5, sticky="w")
        self.port_entry.insert(0, 50007)

        self.username_label = ttk.Label(self.frame, text="Username: ")
        self.username_label.grid(column=0, row=6, sticky="e")
        self.username_entry = ttk.Entry(self.frame)
        self.username_entry.grid(column=1, row=6, sticky="w")

        self.previous_self_button = ttk.Button(self.frame, text="Previous Self", command=lambda: self.get_previous("self"))
        self.previous_self_button.grid(column=0, row=7)

        self.previous_peer_button = ttk.Button(self.frame, text="Previous Peer", command=lambda: self.get_previous("peer"))
        self.previous_peer_button.grid(column=0, row=8)
    
        self.autofill_button = ttk.Button(self.frame, text="Autofill", command=lambda: self.autofill())
        self.autofill_button.grid(column=1, row=7)

        self.submit_button = ttk.Button(self.frame, text="Submit", command=lambda: self.submit_ip_port())
        self.submit_button.grid(column=1, row=8)

        self.screen.mainloop()
        return (self.ip, self.port, self.username)
        
    def get_previous(self, self_or_peer):
        with open("code/addresses.json", "r") as infile:
            addresses = json.load(infile)

        ip = addresses["previous_"+self_or_peer]["ip"]
        port = addresses["previous_"+self_or_peer]["port"]

        self.insert_ip_port(ip,port)

    def autofill(self):
        ip = socket.gethostbyname(socket.gethostname())
        port = 50007

        self.insert_ip_port(ip, port)

    def insert_ip_port(self, ip, port):
        self.ip_entry.delete(0, "end")
        self.ip_entry.insert(0, ip)
        self.port_entry.delete(0, "end")
        self.port_entry.insert(0, port)

    def submit_ip_port(self):
        self.ip = self.ip_entry.get()
        self.port = int(self.port_entry.get())
        self.username = self.username_entry.get()

        # Input validation code coming soon!

        self.screen.destroy()

    # def waiting_for_peer(self):
    #     self.screen = Tk()
    #     self.screen.title("Awaiting Connection")
    #     self.frame = ttk.Frame(self.screen, padding=10)
    #     self.text = ttk.Label(self.frame, text=f"Session started on {self.ip}:{self.port}.\nWaiting for peer to connect.")

    #     self.screen.mainloop()
