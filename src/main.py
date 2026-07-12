import tkinter as tk
from PIL import Image, ImageTk
from kitty import Kitty

# main window
window = tk.Tk()

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

pet = Kitty(window, '../assets/sprites/Idle.png')
pet.animate()

window.bind("<Escape>", lambda event: window.destroy())

window.mainloop()