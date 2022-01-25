import re
import json
import socket

from tkinter import *
from tkinter import ttk

class ConnectionGUI():

    def input_session_type(self):
        # Initialize the window
        self.screen = Tk()
        # Name the window
        self.screen.title("Session Type")

        # Insert a frame and have it display by grid
        self.frame = ttk.Frame(self.screen, padding=10)
        self.frame.grid()

        # Adds a start button and instructions. When the start button is pressed it will call submit_session and passes start to it
        self.start_button = ttk.Button(self.frame, text="START", command=lambda:self.submit_session_type("start"))
        self.start_button.grid(column=0, row=0)
        self.start_instructions = ttk.Label(self.frame, text="Start a session that a \npeer can connect to.")
        self.start_instructions.grid(column=0, row=1, padx=10)

        # Adds a connect button and instructions. When the connect button is pressed it will call submit_session and passes connect to it
        self.connect_button = ttk.Button(self.frame, text="CONNECT", command=lambda: self.submit_session_type("connect"))
        self.connect_button.grid(column=1, row=0)
        self.connect_instructions = ttk.Label(self.frame, text="Connect to a peer that \nhas started a session." )
        self.connect_instructions.grid(column=1, row=1, padx=10)

        # Starts the GUI and loops it to stay up and running
        self.screen.mainloop()

        # Returns the collected info so it can be stored
        return self.session_type

    def submit_session_type(self, type):
        # Store the session type
        self.session_type = type

        # Stop the GUI loop, allowing info to be returned
        self.screen.destroy()

    def input_session_ip_port(self):
        # Initialize the window
        self.screen = Tk()
        # Name the window
        self.screen.title("Session Address")

        # Insert a frame and have it display by grid
        self.frame = ttk.Frame(self.screen, padding=10)
        self.frame.grid()

        # Displays instructions based on what type of session was chosen
        if self.session_type == "start":
            self.intro_label = ttk.Label(self.frame, text="Enter your device's IP address and desired port (default is 50007).")
        elif self.session_type == "connect":
            self.intro_label = ttk.Label(self.frame, text="Enter the IP address and port (default is 50007) of the peer device you are trying to connect to.")
        self.intro_label.grid(column=0, row=0, columnspan=2)

        # Explains the various buttons
        self.username_info = ttk.Label(self.frame, text="If you would like to hide your IP address, please enter a username.")
        self.username_info.grid(column=0, row=1, columnspan=2)

        self.autofill_label = ttk.Label(self.frame, text="Autofill will attempt to autofill your device's IP addres, but verify it for accuracy.")
        self.autofill_label.grid(column=0, row=2, columnspan=2)

        self.previous_label = ttk.Label(self.frame, text="You can also use a previous entry if you have connected before.")
        self.previous_label.grid(column=0, row=3, columnspan=2)

        # Create an entry form for IP address and insert example IP
        self.ip_label = ttk.Label(self.frame, text="IP: ")
        self.ip_label.grid(column=0, row=4, sticky="e")
        self.ip_entry = ttk.Entry(self.frame)
        self.ip_entry.grid(column=1, row=4, sticky="w")
        self.ip_entry.insert(0, "127.0.0.1")

        # Create an entry form for port and insert default port
        self.port_label = ttk.Label(self.frame, text="Port: ")
        self.port_label.grid(column=0, row=5, sticky="e")
        self.port_entry = ttk.Entry(self.frame)
        self.port_entry.grid(column=1, row=5, sticky="w")
        self.port_entry.insert(0, 50007)

        # Create an entry form for a username
        self.username_label = ttk.Label(self.frame, text="Username: ")
        self.username_label.grid(column=0, row=6, sticky="e")
        self.username_entry = ttk.Entry(self.frame)
        self.username_entry.grid(column=1, row=6, sticky="w")

        # Creates a button that when clicked it will insert previous self
        self.previous_self_button = ttk.Button(self.frame, text="Previous Self", command=lambda: self.get_previous("self"))
        self.previous_self_button.grid(column=0, row=7)

        # Creates a button that when clicked it will insert previous peer
        self.previous_peer_button = ttk.Button(self.frame, text="Previous Peer", command=lambda: self.get_previous("peer"))
        self.previous_peer_button.grid(column=0, row=8)
    
        # Creates a button that will attempt to automatically collect the IP address
        self.autofill_button = ttk.Button(self.frame, text="Automatic", command=lambda: self.autofill())
        self.autofill_button.grid(column=1, row=7)

        # Creates a button that will store the info, destroy the GUI, and return the info
        self.submit_button = ttk.Button(self.frame, text="Submit", command=lambda: self.submit_ip_port())
        self.submit_button.grid(column=1, row=8)

        #  Starts the GUI and loops it to stay up and running
        self.screen.mainloop()

        # Returns the selected info
        return (self.ip, self.port, self.username)
        
    def get_previous(self, self_or_peer):
        # Attempts to collect previous info
        try:
            # Opens the file and stores it as a dictionary
            with open("code/addresses.json", "r") as infile:
                addresses = json.load(infile)

            # Pulls out the necessary info
            ip = addresses["previous_"+self_or_peer]["ip"]
            port = addresses["previous_"+self_or_peer]["port"]

            # Calls a function to insert this info
            self.insert_ip_port(ip,port)

        # If no previous info it prints an error statement
        except:
            print("There are no previous entries.")

    def autofill(self):
        # Attempt to collect IP address automatically
        ip = socket.gethostbyname(socket.gethostname())
        # Specifies the default port
        port = 50007

        # Calls a function to insert this info
        self.insert_ip_port(ip, port)

    def insert_ip_port(self, ip, port):
        # Delete current IP entry
        self.ip_entry.delete(0, "end")
        # Insert the selected IP
        self.ip_entry.insert(0, ip)
        # Delete the current port entry
        self.port_entry.delete(0, "end")
        # Insert the selected port
        self.port_entry.insert(0, port)

    def submit_ip_port(self):
        # Stores the collected info so that it can be returned
        self.ip = self.ip_entry.get()
        self.port = int(self.port_entry.get())
        self.username = self.username_entry.get()

        # Input validation code coming soon!

        # Stop the GUI loop, allowing info to be returned
        self.screen.destroy()

    # Function I decided not to input
    # def waiting_for_peer(self):
    #     self.screen = Tk()
    #     self.screen.title("Awaiting Connection")
    #     self.frame = ttk.Frame(self.screen, padding=10)
    #     self.text = ttk.Label(self.frame, text=f"Session started on {self.ip}:{self.port}.\nWaiting for peer to connect.")

    #     self.screen.mainloop()
