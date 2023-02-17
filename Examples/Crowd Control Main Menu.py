import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

class App(tk.Tk):
    def __init__(self, icon_path, bg_path):
        super().__init__()
        self.icon_path = icon_path
        self.bg_path = bg_path
        self.title("My App")
        self.geometry("400x300")
        self.resizable(False, False)
        self.configure(background='white')
        
        # Set the window icon
        self.icon = ImageTk.PhotoImage(Image.open(self.icon_path))
        self.tk.call('wm', 'iconphoto', self._w, self.icon)

        # Set the background image
        self.bg_image = ImageTk.PhotoImage(Image.open(self.bg_path).resize((400, 300), Image.ANTIALIAS))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add the buttons
        self.button1 = ttk.Button(self, text="Launch Game", command=self.run_script1)
        self.button1.place(relx=0.5, rely=0.35, anchor="center")
        self.button2 = ttk.Button(self, text="Settings", command=self.run_script2)
        self.button2.place(relx=0.5, rely=0.5, anchor="center")
        self.button3 = ttk.Button(self, text="Exit", command=self.run_script3)
        self.button3.place(relx=0.5, rely=0.65, anchor="center")

    def run_script1(self):
        subprocess.run(["python", "path/to/script1.py"])

    def run_script2(self):
        subprocess.run(["python", r"C:\Users\Mike\Desktop\OpenGOAL\GitHub\OpenGoal-Crowd-Control-Launcher\Examples\Settings Main Menu.py"])

    def run_script3(self):
        self.destroy()

if __name__ == "__main__":
    app = App(icon_path=r"C:\Users\Mike\Desktop\folder7\yummy.PNG", bg_path=r"C:\Users\Mike\Desktop\folder7\yummy.PNG")
    app.mainloop()
