import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path
from pynput import mouse
from kitty import Kitty

idle_path = Path('../assets')/'sprites'/'Idle.png'
run_path = Path('../assets')/'sprites'/'Running.png'
box_path = Path('../assets')/'sprites'/'Box1.png'

# main window
window = tk.Tk()
screen_width = window.winfo_screenwidth()  # 1536
screen_height = window.winfo_screenheight() # 864

window.title("Desktop Pet")
# # window width and height
# window.geometry("300x300")
# removes window decorations
window.overrideredirect(True)
window.attributes("-topmost", True)

# magenta bc it is unlikely to appear on the sprite
transparent_color = 'magenta'
# makes the window transparent
window.configure(bg=transparent_color)
window.attributes('-transparentcolor', transparent_color)

# create the pet object
pet = Kitty(window, idle_path, run_path, box_path)
pet.x = (screen_width - pet.height) // 2
pet.y = (screen_height  - 45) - pet.height
window.geometry(f"+{pet.x}+{pet.y}")
pet.label.bind("<Button-1>", pet.set_target_left)
pet.label.bind("<Button-3>", pet.set_target_right)

pet.animate()
pet.move()

window.mainloop()