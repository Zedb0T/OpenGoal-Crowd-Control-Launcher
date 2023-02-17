import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import sys


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename
        
class App(tk.Tk):

    def __init__(self, icon_path, bg_path):
        super().__init__()
        self.icon_path = icon_path
        self.bg_path = bg_path
        self.title("Jak and Daxter Crowd Control Launcher")
        self.geometry("400x300")
        self.resizable(False, False)
        self.configure(background='white')
        
        # Set the window icon
        self.icon = ImageTk.PhotoImage(Image.open(self.icon_path))
        self.tk.call('wm', 'iconphoto', self._w, self.icon)

        # Set the background image
        self.bg_image = ImageTk.PhotoImage(Image.open(self.bg_path).resize((800, 450), Image.Resampling.LANCZOS))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add the buttons
        self.button1 = ttk.Button(self, text="Launch Game", command=self.run_script1, width=15)
        self.button1.place(relx=0.5, rely=0.35, anchor="center")
        self.button2 = ttk.Button(self, text="Settings", command=self.run_script2, width=15)
        self.button2.place(relx=0.5, rely=0.5, anchor="center")
        self.button3 = ttk.Button(self, text="Exit", command=self.run_script3, width=15)
        self.button3.place(relx=0.5, rely=0.65, anchor="center")

    def run_script1(self):
        subprocess.run(["python", "path/to/script1.py"])
        print(bg_path)

    def run_script2(self):
        subprocess.run(["python", "Settings Main Menu.py"])

    def run_script3(self):
        self.destroy()



if getattr(sys, "frozen", False):
    # If we are a pyinstaller exe get the path of this file, not python
    fileRoot = sys._MEIPASS
else:
    # if we are running the .py directly use this path
    fileRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) 
    
images_dir = os.path.join(fileRoot, "Images") 

icon_path = get_path(os.path.join(images_dir, "appicon.ico"))
bg_path = get_path(os.path.join(images_dir, "Launcher_BG.png"))

# ...

if __name__ == "__main__":
    app = App(icon_path=icon_path, bg_path=bg_path)
    
    app.mainloop()
