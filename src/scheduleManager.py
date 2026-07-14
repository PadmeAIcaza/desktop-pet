import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
from datetime import datetime

class ScheduleManager:
    def __init__(self, window):
        self.window = window
        self.input_window = None
        self.file_path = 'schedule.json'
        self.time = 0

    def open_schedule_editor(self, _):
        BG = '#F4D8DA'
        self.input_window = tk.Toplevel(self.window)
        self.input_window.configure(bg=BG)
        self.input_window.title('Add Remainder')
        self.input_window.geometry('320x180')

        tk.Label(self.input_window, text='Date (MM-DD): ', font=("Times New Roman", 10), bg=BG).pack()
        date_entry = (tk.Entry(self.input_window, width=10))
        date_entry.pack()

        tk.Label(self.input_window, text='Time (HH:MM): ', font=("Times New Roman", 10), bg=BG).pack()
        time_entry = (tk.Entry(self.input_window, width=10))
        time_entry.pack()

        tk.Label(self.input_window, text='Task: ', font=("Times New Roman", 10), bg=BG).pack()
        task_entry = (tk.Entry(self.input_window, width=40))
        task_entry.pack()

        def save_button_pressed():
            date_text = date_entry.get().strip()
            time_text = time_entry.get().strip()
            task_text = task_entry.get().strip()
            if time_text == '' or task_text == '' or date_text == '':
                messagebox.showerror(title='Empty Fields', message='Please fill every field')
                return
            is_ok = messagebox.askokcancel(title='Confirm', message=f'This is the schedule entered: \nTime: {time_text}\nTask: {task_text}\nIs this ok to save?')
            if is_ok:
                self.add_schedule(date_text, time_text, task_text)
                self.input_window.destroy()

        reminder_image = Image.open('../assets/addreminder.png').resize((150, 40), Image.Resampling.LANCZOS)
        self.addreminder = ImageTk.PhotoImage(reminder_image)
        save_button = tk.Button(self.input_window, image=self.addreminder, text='Add Reminder', compound='center', fg='black', font=("Times New Roman", 10, "bold"), bd=0, highlightthickness=0, bg=BG, activebackground=BG, command=save_button_pressed)
        save_button.pack()

    def load_schedule(self):
        try:
            with open(self.file_path, mode='r') as file:
                return json.load(file)  # reads old data
        except FileNotFoundError:
            return {'schedule':[]}
        except json.JSONDecodeError:
            return {'schedule': []}

    def save_schedule(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def add_schedule(self, date_text, time_text, task_text):
        data = self.load_schedule()
        new_task = {
            "date": date_text,
            'time': time_text,
            'task': task_text,
            'completed': False
        }

        data['schedule'].append(new_task)
        data['schedule'].sort(key=lambda task: datetime.strptime(f'{task['date']} {task['time']}', '%m-%d %H:%M'))
        self.save_schedule(data)

    def complete_next_task(self):
        schedule_list = self.load_schedule()
        schedule = schedule_list['schedule']
        for task in schedule:
            if not task.get('completed', False):
                task['completed'] = True
                self.save_schedule(schedule_list)
                return task
        return None

    def get_next_task(self):
        schedule_list = self.load_schedule()
        schedule = schedule_list['schedule']
        for task in schedule:
            if not task['completed']:
                return task
        return None

    def is_task_late(self, task):
        current_time = datetime.now().time()
        task_time = datetime.strptime(task['time'], '%H:%M').time()

        return current_time > task_time and not task['completed']







