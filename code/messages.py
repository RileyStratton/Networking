import time

from threading import Thread
from messages_gui import MessagesGUI

class Messages():
    def __init__(self, sock, username):
        # Store sock so that messages can be sent and received
        self.sock = sock
        
        # Uses IP as username if there is none
        if username == "":
            self.username_self = self.sock.getsockname()[0]

        # Uses username provided if there is one
        else:
            self.username_self = username

        # Sends username_self so that it can be stored by the other device
        self.sock.sendall(self.username_self.encode())

        # Stores username of the other device
        self.username_peer = self.sock.recv(1024).decode()

        # Initializes a blank list to store and display messages
        self.message_list = []

        # Creates a thread that will check for new messages every quarter second
        t1 = Thread(target=self.receive_message)
        t1.setDaemon(True)
        t1.start()

        # Initializes MessagesGUI and the rest runs from there. The current Messages object is sent to be displayed.
        self.messages_gui = MessagesGUI(self)


    # The thread will repeatedly run this to receive messages
    def receive_message(self):
        while True:
            # Message is appended to messge list. The list is used to display all messages
            self.message_list.append(self.sock.recv(1024).decode())
            time.sleep(.25)

    # This function is ran when the GUI's send button is clicked
    def send_message(self, message):
        # Attaches username to the front of the message
        msg = f"{self.username_self}: {message}"
        # The message is appended to the message list. The list is used to display all messages
        self.message_list.append(msg)
        # Message is sent to the other device
        self.sock.sendall(msg.encode())
        



