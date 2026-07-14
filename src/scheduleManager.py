import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

class ScheduleManager:
    def __init__(self, window):
        self.window = window
        self.input_window = None
        self.file_path = 'schedule.json'
        self.time = 0

    def open_schedule_editor(self, _):
        BG = '#FDEB9E'
        self.input_window = tk.Toplevel(self.window)
        self.input_window.configure(bg=BG)
        self.input_window.title('Add Remainder')
        self.input_window.geometry('320x180')

        tk.Label(self.input_window, text='Time (HH:MM):', bg=BG).pack()
        time_entry = (tk.Entry(self.input_window, width=10))
        time_entry.pack()

        tk.Label(self.input_window, text='Task: ', bg=BG).pack()
        task_entry = (tk.Entry(self.input_window, width=40))
        task_entry.pack()

        def save_button_pressed():
            time_text = time_entry.get().strip()
            task_text = task_entry.get().strip()
            if time_text == '' or task_text == '':
                messagebox.showerror(title='Empty Fields', message='Please fill every field')
                return
            is_ok = messagebox.askokcancel(title='Confirm', message=f'This is the schedule entered: \nTime: {time_text}\nTask: {task_text}\nIs this ok to save?')
            if is_ok:
                self.add_schedule(time_text, task_text)
                self.input_window.destroy()

        save_button = tk.Button(self.input_window, text='Save Remainder', command=save_button_pressed)
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

    def add_schedule(self, time_text, task_text):
        data = self.load_schedule()
        new_task = {
            'time': time_text,
            'task': task_text,
            'completed': False
        }

        data['schedule'].append(new_task)
        data['schedule'].sort(key=lambda task: task["time"])
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







