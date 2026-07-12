import tkinter as tk
from PIL import Image, ImageTk
from kitty import Kitty

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
pet = Kitty(window, '../assets/sprites/Idle.png')
#
x = (screen_width - pet.height) // 2
y = (screen_height  - 48) - pet.height
window.geometry(f"+{x}+{y}")
pet.animate()

# closes the app after pressing esc
window.bind("<Escape>", lambda event: window.destroy())

window.mainloop()