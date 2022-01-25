from tkinter import *
from tkinter import ttk

class MessagesGUI():
    def __init__(self, messages):
        self.messages = messages

        self.main_gui()

    def main_gui(self):
        self.screen = Tk()
        self.screen.title("IP Messaging")

        self.info = ttk.Label(self.screen, text=f"Chatting with {self.messages.username_peer}")
        self.info.pack(side=TOP)
        self.send_button = ttk.Button(self.screen, text="Send", command=self.send_helper)
        self.send_button.pack(side=BOTTOM)

        self.send_bar = ttk.Entry(self.screen, width=60, command=self.send_helper)
        self.send_bar.pack(side=BOTTOM)
        self.send_bar.insert(0, "Type your message and press enter to send!")

        self.scrollbar = Scrollbar(self.screen)
        self.scrollbar.pack(side= RIGHT, fill=Y)
        
        self.message_box = Listbox(self.screen, yscrollcommand=self.scrollbar.set, width=60, height=40)

        self.display_messages()

        self.message_box.pack()
        self.scrollbar.config(command=self.message_box.yview)

        self.screen.mainloop()

    def display_messages(self):
        self.message_box.delete(0, "end")
        for message in self.messages.message_list:
            self.message_box.insert(END, message)
        self.screen.after(250, self.display_messages)

    def send_helper(self):
        message = self.send_bar.get()
        self.send_bar.delete(0,"end")
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