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
        self.send_button = ttk.Button(self.screen, text="Send", command=lambda: self.messages.send_message(self.send_bar.get()))
        self.send_button.pack(side=BOTTOM)

        self.send_bar = ttk.Entry(self.screen, width=60)
        self.send_bar.pack(side=BOTTOM)

        self.scrollbar = Scrollbar(self.screen)
        self.scrollbar.pack(side= RIGHT, fill=Y)
        
        self.message_box = Listbox(self.screen, yscrollcommand=self.scrollbar.set, width=60, height=40)

        self.display_messages()        

        self.message_box.pack()
        self.scrollbar.config(command=self.message_box.yview)

        self.screen.after(500, self.display_messages)

        self.screen.mainloop()

    def display_messages(self):
        for message in self.messages.message_list:
            self.message_box.insert(END, message)