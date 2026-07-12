import tkinter as tk
from PIL import Image, ImageTk

class Kitty:
    def __init__(self, window, idle_path, run_path):
        # save the window so other methods can access it
        self.window = window
        # sprite sheet info (384x64, so 6 frames of 64x64
        self.frame_width = 64
        self.frame_height = 64
        # pet's dimensions and position
        self.width = self.frame_width
        self.height = self.frame_height
        self.x = 0
        self.y = 0
        self.speed = 4
        self.direction = 1 # 1 right, -1 left
        self.target_x = 0
        self.is_moving = False
        self.move_distance = int(self.window.winfo_fpixels("4c")) # converts 3 centimeters into pixels for this display.
        # save the screen width so the cat knows where the edge is.
        self.screen_width = self.window.winfo_screenwidth()
        # stores all of the pet's animations
        self.animations = {}
        self.current_frame = 0
        self.animations['idle'] = self.load_animation(idle_path)
        self.animations['run'] = self.load_animation(run_path)
        self.current_animation = 'idle'

        self.label = tk.Label(self.window, image=self.animations["idle"]['right'][0], bg="magenta", borderwidth=0)
        self.label.pack()

    def load_animation(self, run_path):
        # open sprite sheet using Pillow
        sprite_sheet = Image.open(run_path)
        frame_count = sprite_sheet.width // self.frame_width
        # holds every separate frame
        frames_right = []
        frames_left = []
        for index in range(frame_count):
            left = index * self.frame_width # frame 0 starts at x=0, frame 1 starts at x=64, frame 3 starts at x=128
            top = 0 # the sheet is only one row tall, so every frame starts at the top
            right = left + self.frame_width
            bottom = self.frame_height
            # crop ONE frame out of the sprite sheet
            frame = sprite_sheet.crop((left, top, right, bottom))
            # then convert it into a Tkinter image and store it
            frames_right.append(ImageTk.PhotoImage(frame))
            # flip the frame horizontally and store it
            flipped_frame = frame.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            frames_left.append(ImageTk.PhotoImage(flipped_frame))
        return {
            'right': frames_right,
            'left': frames_left
        }

    def change_animation(self, animation_name):
        if self.current_animation == animation_name:
            return # avoids restarting the animation if it is already active

        self.current_animation = animation_name
        self.current_frame

    def animate(self):
        # choose which direction's frames to display
        if self.direction == 1:
            facing = 'right'
        else:
            facing = 'left'
        # get the frames for the animation currenlty playing
        frames = self.animations[self.current_animation][facing]
        # move to the next frame, when the last frame is reached, return to frame 0
        self.current_frame = (self.current_frame + 1) % len(frames)
        # update the image displayed by the label
        self.label.configure(image=frames[self.current_frame])

        self.window.after(150, self.animate)

    def move(self):
        if self.is_moving:
            self.change_animation("run")
            # calculate the remaining horizontal distance.
            distance = self.target_x - self.x
            # stop when the remaining distance is smaller than one movement.
            if abs(distance) <= self.speed:
                self.x = self.target_x
                self.is_moving = False
                self.change_animation("idle")
            else:
                # move toward the target.
                self.x += self.speed * self.direction
            self.window.geometry(f"+{self.x}+{self.y}")
        else:
            self.change_animation("idle")

        self.window.after(20, self.move)

    def set_target(self, event):
        # horizontal center of the cat on the screen.
        cat_center_x = self.x + (self.width // 2)
        # mouse position relative to the entire screen.
        mouse_x = event.x_root
        if mouse_x > cat_center_x:
            # mouse is to the right of the cat.
            self.direction = 1
            self.target_x = self.x + self.move_distance
        elif mouse_x < cat_center_x:
            # mouse is to the left of the cat.
            self.direction = -1
            self.target_x = self.x - self.move_distance
        else:
            # the mouse is exactly in the center, so do nothing.
            return
        # prevent the target from going beyond either screen edge.
        self.target_x = max(0,min(self.target_x, self.screen_width - self.width))
        # tell move() that the cat should start running.
        self.is_moving = True