import tkinter as tk
from PIL import Image, ImageTk

class ChatBox:
    def __init__(self, window, chatbox_path):
        self.window = window
        image = Image.open(chatbox_path)
        self.chatbox_image = ImageTk.PhotoImage(image)
        self.chatbox = tk.Label(self.window, image=self.chatbox_image, bg="magenta", borderwidth=0)
        self.text_label = tk.Label(self.window, text='', bg='#f7e8e8', font=('Arial', 9), wraplength=75, justify='center')

    def show(self, message):
        self.text_label.configure(text=message)
        self.chatbox.place(x=49, y=50)
        self.text_label.place(x=80, y=65)
        # hide after 2 seconds
        self.window.after(2000, self.hide)

    def hide(self):
        self.chatbox.place_forget()
        self.text_label.place_forget()

