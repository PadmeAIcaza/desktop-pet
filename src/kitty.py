import tkinter as tk
from PIL import Image, ImageTk

class Kitty:
    def __init__(self, window, sprite_path):
        # save the window so other methods can access it
        self.window = window

        # sprite sheet info (384x64, so 6 frames of 64x64
        self.frame_width = 64
        self.frame_height = 64
        # pet's dimensions
        self.width = self.frame_width
        self.height = self.frame_height
        self.current_frame = 0
        # stores all of the pet's animations
        self.animations = {}
        self.animations['idle'] = self.load_animation(sprite_path)
        self.current_animation = 'idle'

        self.label = tk.Label(self.window, image=self.animations["idle"][0], bg="magenta", borderwidth=0)
        self.label.pack()

    def load_animation(self, sprite_path):
        # open sprite sheet using Pillow
        sprite_sheet = Image.open(sprite_path)
        frame_count = sprite_sheet.width // self.frame_width
        # holds every separate frame
        frames = []
        for index in range(frame_count):
            left = index * self.frame_width # frame 0 starts at x=0, frame 1 starts at x=64, frame 3 starts at x=128
            top = 0 # the sheet is only one row tall, so every frame starts at the top
            right = left + self.frame_width
            bottom = self.frame_height
            # crop ONE frame out of the sprite sheet
            frame = sprite_sheet.crop((left, top, right, bottom))
            # then convert it into a Tkinter image and store it
            frames.append(ImageTk.PhotoImage(frame))
        return frames

    def animate(self):
        # get the frames for the animation currenlty playing
        frames = self.animations[self.current_animation]
        # move to the next frame, when the last frame is reached, return to frame 0
        self.current_frame = (self.current_frame + 1) % len(frames)
        # update the image displayed by the label
        self.label.configure(image=frames[self.current_frame])

        self.window.after(150, self.animate)
