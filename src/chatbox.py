import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from scheduleManager import ScheduleManager

class ChatBox:
    def __init__(self, window, chatbox_path):
        BG = '#F4D8DA'
        self.window = window
        self.schedule_manager = ScheduleManager(self.window)
        image = Image.open(chatbox_path)
        self.chatbox_image = ImageTk.PhotoImage(image)
        self.chatbox = tk.Label(self.window, image=self.chatbox_image, bg="magenta", borderwidth=0)
        self.text_label = tk.Label(self.window, text='', bg=BG, font=('Arial', 9), wraplength=75, justify='center')
        self.button = Button(window, text="✓", width=5, command=self.task_completed, pady=0)

    def show(self, message):
        self.text_label.configure(text=message)
        self.chatbox.place(x=49, y=10)
        self.text_label.place(x=80, y=25)
        self.button.place(x=80, y=65)
        # hide after 2 seconds
        self.window.after(2000000000, self.hide)

    def display_task(self):
        next_task = self.schedule_manager.get_next_task()
        if next_task:
            self.text_label.config(text=f'{next_task['time']}\n{next_task['task']}')

    def task_completed(self):
        completed_task = self.schedule_manager.complete_next_task()
        self.display_task()
        # if completed_task:
        #     self.display_task()

    def hide(self):
        self.chatbox.place_forget()
        self.text_label.place_forget()
        self.button.place_forget()

