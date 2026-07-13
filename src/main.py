import tkinter as tk
from pathlib import Path
from kitty import Kitty

idle_path = Path('../assets')/'sprites'/'Idle.png'
run_path = Path('../assets')/'sprites'/'Running.png'
cuddle_path = Path('../assets')/'sprites'/'Happy.png'
sleeping_path = Path('../assets')/'sprites'/'Sleeping.png'
surprised_path = Path('../assets')/'sprites'/'Surprised.png'

# main window
window = tk.Tk()
screen_width = window.winfo_screenwidth()  # 1536
screen_height = window.winfo_screenheight() # 864

window.title("Desktop Pet")
# window width and height
# removes window decorations
window.overrideredirect(True)
window.attributes("-topmost", True)

# magenta bc it is unlikely to appear on the sprite
transparent_color = 'magenta'
# makes the window transparent
window.configure(bg=transparent_color)
window.attributes('-transparentcolor', transparent_color)

# create the pet object
pet = Kitty(window, idle_path, run_path, cuddle_path, sleeping_path, surprised_path)
pet.x = (screen_width - pet.height) // 2
pet.y = (screen_height  - 45) - pet.height
window.geometry(f"+{pet.x}+{pet.y}")
# clicks functionality
pet.label.bind("<Button-1>", pet.set_target_left)
pet.label.bind("<Button-2>", pet.start_cuddles)
pet.label.bind("<Button-3>", pet.set_target_right)
pet.label.bind("<Enter>", pet.wake_up)
pet.animate()
pet.move()
pet.check_idle()

window.bind("<Escape>", lambda event: window.destroy())

window.mainloop()