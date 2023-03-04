import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import sys
from EnvFileUpdater import EnvFileChecker



def get_parent_directory():
    """Returns the parent directory of the script or the app data location of the system if it's a PyInstaller exe,
    but if it contains the word "Release" in its path it returns the location of the PyInstaller exe."""
    if getattr(sys, 'frozen', False):
        # The application is a PyInstaller executable.
        if "Release" in sys.executable:
            return os.path.dirname(sys.executable)
        else:
            return os.path.abspath(os.path.join(os.path.dirname(sys.executable), os.pardir))
    else:
        # The script is being run in a Python interpreter.
        return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    
parent_dir = get_parent_directory()



print(os.getcwd())
#hack


#root data folder is 
#appdata_dir = os.getenv("APPDATA")
og_dir = os.path.join(os.getenv("APPDATA"), "OpenGOAL-CrowdControl","")


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename
    
def init():
    paths_to_check = ["env/command_enabled.env",
                      "env/command_durations.env",
                      "env/command_cooldowns.env",
                      "env/twitch_settings.env",
                      "env/unused.env"]
    for path in paths_to_check:
        checker = EnvFileChecker(path)
        checker.check_or_create()
    
    checker.addENVtwitchSettings()
    checker.addENVcommandDurations()
    checker.addENVcommandEnabled()
    checker.addENVcommandCooldown()

class App(tk.Tk):
    
    def __init__(self, icon_path, bg_path):
        super().__init__()
        init()
        self.icon_path = icon_path
        self.bg_path = bg_path
        self.title("Jak and Daxter Crowd Control Launcher")
        self.geometry("400x300+{}+{}".format(self.winfo_screenwidth() // 2 - 200, self.winfo_screenheight() // 2 - 150))
        self.resizable(False, False)
        self.configure(background='white')
        self.state = "normal"  # keep track of the current state of the window
        # Set the window icon
        self.icon = ImageTk.PhotoImage(Image.open(self.icon_path))
        self.tk.call('wm', 'iconphoto', self._w, self.icon)

        # Set the background image
        self.bg_image = ImageTk.PhotoImage(Image.open(self.bg_path).resize((800, 450), Image.Resampling.LANCZOS))
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add the buttons
        self.button1 = ttk.Button(self, text="Launch Game", command=self.run_Game, width=15)
        self.button1.place(relx=0.5, rely=0.35, anchor="center")
        self.button2 = ttk.Button(self, text="Settings", command=self.run_SettingsMenu, width=15)
        self.button2.place(relx=0.5, rely=0.5, anchor="center")
        self.button3 = ttk.Button(self, text="Exit", command=self.run_Exit, width=15)
        self.button3.place(relx=0.5, rely=0.65, anchor="center")

        # Bind the F12 key to the toggle_fullscreen method
        self.bind("<F12>", self.toggle_fullscreen)



    def toggle_fullscreen(self, event=None):
        if self.state == "normal":
            # Save the original size and position of the window
            self.normal_geometry = self.geometry()

            # Resize the window to fill the screen
            self.state = "fullscreen"
            self.attributes("-fullscreen", True)

            # Resize the background image to fill the screen
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            bg_image = Image.open(self.bg_path).resize((screen_width, screen_height), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(bg_image)
            self.bg_label.config(image=self.bg_image)
        else:
            # Restore the original size and position of the window
            self.state = "normal"
            self.attributes("-fullscreen", False)
            self.geometry(self.normal_geometry)

            # Resize the background image to fit the original size of the window
            bg_image = Image.open(self.bg_path).resize((800, 450), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(bg_image)
            self.bg_label.config(image=self.bg_image)


    def run_Game(self):
        settings_windowObj = settings_windowObj
        settings_window = settings_windowObj.get_settings_window()
        settings_window.mainloop()


    def run_SettingsMenu(self):
        self.destroy()
        settings_path = os.path.join(fileRoot, "Examples", "Settings Main Menu.py")
        subprocess.run(["python", settings_path])
        

    def run_Exit(self):
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
