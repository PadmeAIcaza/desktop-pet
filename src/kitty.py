import tkinter as tk
from PIL import Image, ImageTk

class Kitty:
    def __init__(self, window, sprite_path):
        # save the window so other methods can access it
        self.window = window

        # sprite sheet info (384x64, so 6 frames of 64x64
        self.frame_width = 64
        self.frame_height = 64
        self.frame_count = 6
        self.current_frame = 0

        # open sprite sheet using Pillow
        sprite_sheet = Image.open(sprite_path)
        # holds every separate frame
        self.frames = []

        for index in range(self.frame_count):
            left = index*self.frame_width # frame 0 starts at x=0, frame 1 starts at x=64, frame 3 starts at x=128
            top = 0
            right = left+self.frame_width
            bottom = self.frame_height

            frame = sprite_sheet.crop((left, top, right, bottom))
            self.frames.append(ImageTk.PhotoImage(frame))

        self.label = tk.Label(self.window, image=self.frames[0], bg='magenta', borderwidth=0)

        self.label.pack()

    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.label.configure(image=self.frames[self.current_frame])
        self.window.after(150, self.animate)