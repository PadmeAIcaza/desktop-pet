import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from scheduleManager import ScheduleManager

class ChatBox:
    def __init__(self, window, chatbox_path):
        BG = '#F4D8DA'
        self.window = window
        # self.frame = Frame(window)
        # self.label = Label(self.frame, text="")
        # self.label.pack()
        self.schedule_manager = ScheduleManager(self.window)
        image = Image.open(chatbox_path).resize((200, 100), Image.Resampling.LANCZOS)
        self.chatbox_image = ImageTk.PhotoImage(image)
        self.chatbox = tk.Label(self.window, image=self.chatbox_image, bg="magenta", borderwidth=0)
        # self.chatbox_frame = Frame(window)
        self.text_label = tk.Label(self.window, text='', bg=BG, font=('Arial', 9), wraplength=75, justify='center')
        check_image = Image.open('../assets/checkbutton.png').resize((35, 35), Image.Resampling.LANCZOS)
        self.checkmark = ImageTk.PhotoImage(check_image)
        self.button = Button(window, image=self.checkmark, bd=0, highlightthickness=0, bg=BG, activebackground=BG, command=self.task_completed)
        self.chatbox_x = 8
        self.chatbox_y = 1
        self.text_x = 40
        self.text_y = 15
        self.button_x = 140
        self.button_y = 30

    def show(self, message):
        self.text_label.configure(text=message)
        self.chatbox.place(x=self.chatbox_x, y=self.chatbox_y)
        self.text_label.place(x=self.text_x, y=self.text_y)
        self.button.place(x=self.button_x, y=self.button_y)
        # hide after 2 seconds
        #self.window.after(2000000000, self.hide)

    def display_task(self, event=None):
        next_task = self.schedule_manager.get_next_task()
        if next_task is None:
            message = self.text_label.config(text="No incomplete tasks! ✓")
        elif self.schedule_manager.is_task_late(next_task):
            message = self.text_label.config(text=f'Late:\n{next_task['time']}\n{next_task['task']}')
        else:
            message = self.text_label.config(text=f'{next_task['time']}\n{next_task['task']}')
        self.show(message)

    def task_completed(self):
        completed_task = self.schedule_manager.complete_next_task()
        if completed_task:
            self.display_task()
        self.hide()

    def hide(self):
        self.chatbox.place_forget()
        #self.chatbox_frame.place_forget()
        self.text_label.place_forget()
        self.button.place_forget()

    # def get_upcoming_task(self):
    #     schedule_list = self.schedule_manager.load_schedule()
    #     schedule = schedule_list['schedule']
    #     now = datetime.now()
    #
    #     for task in schedule:
    #         if not task['completed']:
    #             task_time = datetime.strptime(task['time'], '%H:%M')
    #
    #         task_datetime = now.replace(hour=task_time.hour, minute=task_time.minute, second=0, microsecond=0)
    #
    # def check_upcoming_task(self):
    #     next_task = self.schedule_manager.get_next_task()
    #     if next_task is not None:
    #         now = datetime.now()
    #         task_time = datetime.strptime(next_task['time'], "%H:%M")
    #
    #         task_datetime = now.replace(hour=task_time.hour, minute=task_time.minute, second=0, microsecond=0)
    #         minutes_until_task = (task_datetime - now).total_seconds() / 60
    #
    #         if 0 <= minutes_until_task <= 1:
    #             self.display_task(next_task)
    #
    #     self.window.after(60_000, self.check_upcoming_task)



