from messages_gui import MessagesGUI

class Messages():
    def __init__(self, sock, username):
        self.sock = sock
        
        if username == "":
            self.username_self = self.sock.getsockname()[0]
        else:
            self.username_self = username

        self.sock.sendall(self.username_self.encode())
        self.username_peer = self.sock.recv(1024).decode()

        self.message_list = []

        self.messages_gui = MessagesGUI(self)

    def receive_message(self):
        self.message_list.append(self.sock.recv(1024).decode())

    def send_message(self, message):
        msg = f"{self.username_self}: {message}"
        self.message_list.append(msg)
        self.sock.sendall(msg.encode())
        



