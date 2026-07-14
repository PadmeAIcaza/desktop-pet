import tkinter as tk
from PIL import Image, ImageTk
import time

class Kitty:
    def __init__(self, window, chatbox, idle_path, run_path, cuddle_path, sleeping_path, surprised_path):
        # save the window so other methods can access it
        self.window = window
        self.chatbox = chatbox
        self.window_width = 200
        self.window_height = 160
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
        self.state = 'idle'
        self.move_distance = int(self.window.winfo_fpixels("5c")) # converts 4 centimeters into pixels for this display.
        # save the screen width so the cat knows where the edge is.
        self.screen_width = self.window.winfo_screenwidth()
        # stores all of the pet's animations
        self.animations = {}
        self.current_frame = 0
        self.animations['idle'] = self.load_animation(idle_path)
        self.animations['run'] = self.load_animation(run_path)
        self.animations['cuddles'] = self.load_animation(cuddle_path)
        self.animations['sleeping'] = self.load_animation(sleeping_path)
        self.animations['surprised'] = self.load_animation(surprised_path)
        self.current_animation = 'idle'
        self.last_interaction = time.time()

        self.label = tk.Label(self.window, image=self.animations["idle"]['right'][0], bg="magenta", borderwidth=0)
        cat_x = (self.window_width - self.width) // 2 #68
        cat_y = self.window_height - self.height #96
        self.label.place(x=cat_x, y=cat_y)

    def load_animation(self, path):
        # open sprite sheet using Pillow
        sprite_sheet = Image.open(path)
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
        self.current_frame = 0

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
        if self.state == 'sleeping':
            # do not move or replace the sleeping animation.
            pass
        elif self.state == 'surprised':
            # do not move or replace the sleeping animation.
            pass
        elif self.state == 'cuddles':
            # do not move or switch animations while cuddling.
            pass
        elif self.state == 'run':
            self.change_animation(self.state)
            # calculate the remaining horizontal distance.
            distance = self.target_x - self.x
            # stop when the remaining distance is smaller than one movement.
            if abs(distance) <= self.speed:
                self.x = self.target_x
                self.state = 'idle'
                self.change_animation(self.state)
            else:
                # move toward the target.
                self.x += self.speed * self.direction
            self.window.geometry(f"200x160+{self.x}+{self.y}")
        else:
            self.state = 'idle'
            self.change_animation(self.state)

        self.window.after(20, self.move)

    def start_cuddles(self, _):
        self.state = 'cuddles'
        self.change_animation(self.state)
        self.last_interaction = time.time()

        self.window.after(3000, self.end_cuddles)

    def end_cuddles(self):
        self.state = 'idle'
        self.change_animation(self.state)

    def move_fixed_direction(self, direction):
        self.direction = direction
        self.target_x = self.x + (direction * self.move_distance)
        # prevent the target from going beyond either screen edge.
        self.target_x = max(0,min(self.target_x, self.screen_width - self.width))
        # tell move() that the cat should start running.
        self.state = 'run'


    def set_target_right(self, _):
        self.move_fixed_direction(1)
        self.last_interaction = time.time()

    def set_target_left(self, _):
        self.move_fixed_direction(-1)
        self.last_interaction = time.time()

    def check_idle(self):
        current_time = time.time()
        elapsed = current_time - self.last_interaction
        if elapsed > 5:
            self.state = 'sleeping'
            self.change_animation(self.state)

        self.window.after(500, self.check_idle)

    def wake_up(self, _):
        if self.state == 'sleeping':
            self.state = 'surprised'
            self.change_animation(self.state)
            self.last_interaction = time.time()

            self.window.after(800, self.woken_up)

    def woken_up(self):
        if self.state == 'surprised':
            self.state = 'idle'
            self.change_animation(self.state)

    # debbuging
    def talk(self, _):
        self.chatbox.show('Meow!')
        self.last_interaction = time.time()

    # def set_target(self, event):
    #     # horizontal center of the cat on the screen.
    #     cat_center_x = self.x + (self.width // 2)
    #     # mouse position relative to the entire screen.
    #     mouse_x = event.x_root
    #     if mouse_x > cat_center_x:
    #         # mouse is to the right of the cat.
    #         self.direction = 1
    #         self.target_x = self.x + self.move_distance
    #     elif mouse_x < cat_center_x:
    #         # mouse is to the left of the cat.
    #         self.direction = -1
    #         self.target_x = self.x - self.move_distance
    #     else:
    #         # the mouse is exactly in the center, so do nothing.
    #         return
    #     # prevent the target from going beyond either screen edge.
    #     self.target_x = max(0,min(self.target_x, self.screen_width - self.width))
    #     # tell move() that the cat should start running.
    #     self.is_moving = True

