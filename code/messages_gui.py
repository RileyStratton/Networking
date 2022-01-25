from tkinter import *
from tkinter import ttk

class MessagesGUI():
    def __init__(self, messages):
        # Store the messages object to be used for displaying it's info
        self.messages = messages

        self.main_gui()

    def main_gui(self):
        # Initialize the page and sets it's title
        self.screen = Tk()
        self.screen.title("IP Messaging")

        # Displays who you're chatting with at the top of the screen
        self.info = ttk.Label(self.screen, text=f"Chatting with {self.messages.username_peer}")
        self.info.pack(side=TOP)

        # Adds send button to the bottom. When clicked it calls send_helper, which eventually sends the message
        self.send_button = ttk.Button(self.screen, text="Send", command=self.send_helper)
        self.send_button.pack(side=BOTTOM)

        # Adds send bar right above the 
        self.send_bar = ttk.Entry(self.screen, width=60)
        self.send_bar.pack(side=BOTTOM)

        # Adds a scrollbar to the right side
        self.scrollbar = Scrollbar(self.screen)
        self.scrollbar.pack(side= RIGHT, fill=Y)
        
        # Initializes a widget to display the message list in
        self.message_box = Listbox(self.screen, yscrollcommand=self.scrollbar.set, width=60, height=40)

        # Calls a function that adds all messages to the widget
        self.display_messages()

        # Displays the message box and makes the scrollbar work
        self.message_box.pack()
        self.scrollbar.config(command=self.message_box.yview)

        # Starts the GUI and loops it to stay up and running
        self.screen.mainloop()

    def display_messages(self):
        # Clears the current message box
        self.message_box.delete(0, "end")

        # Loops through every message in message_list and adds it to the message box
        for message in self.messages.message_list:
            self.message_box.insert(END, message)

        # Updates the message box every quarter second
        self.screen.after(250, self.display_messages)

    def send_helper(self):
        # Stores the message as a string
        message = self.send_bar.get()
        # Clears the send bar
        self.send_bar.delete(0,"end")
        # Calls the send_message function of the Messages class
        self.messages.send_message(message)
        

# class FakeMessages():
#     def __init__(self):
#         self.message_list = [0,1,2,3,4,5,6,7,8,9,]
#         self.username_self = "Riley"
#         self.username_peer = "April"

#     def send_message(self, message):
#         msg = f"{self.username_self}: {message}"
#         self.message_list.append(msg)
#         print(self.message_list)

#     def receive_message(self):
#         pass

    
# fake_messages = FakeMessages()
# message_gui = MessagesGUI(fake_messages)