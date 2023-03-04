import shutil
import tkinter as tk
import os
from dotenv import dotenv_values
from EnvFileUpdater import EnvFileUpdater
import subprocess
import tempfile
import sys

if getattr(sys, "frozen", False):
    # If we are a pyinstaller exe get the path of this file, not python
    fileRoot = sys._MEIPASS
else:
    # if we are running the .py directly use this path
    fileRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) 

og_dir = os.path.join(os.getenv("APPDATA"), "OpenGOAL-CrowdControl","")

class App(tk.Frame):
    def __init__(self, master=None, env_file_path=None):
        super().__init__(master, padx=20, pady=20)
        self.env_file_path = env_file_path
        self.env_values = dotenv_values(self.env_file_path)
        self.grid()
        self.create_widgets()
        master.title("Twitch Settings")

    def create_widgets(self):
        self.entries = []
        self.labels = []
        row = 0
        col = 0

        font = ('Helvetica', 10)
        btn_font = ('Helvetica', 10, 'bold')

        for key, value in self.env_values.items():
            label = tk.Label(self, text=key.replace("_"," ").title().replace("Msg","Message"), font=font)
            label.grid(row=row, column=col)
            self.labels.append(label)
            entry = tk.Entry(self, width=50)
            entry.insert(0, value)
            entry.grid(row=row, column=col + 1)
            self.entries.append(entry)
            row += 1
            if row == (int(len(self.env_values.items()))):
                row = 0
                col += 2

        self.save_button = tk.Button(self, text="Save", command=self.save, width=15, font=btn_font)
        self.save_button.grid(row=row, column=col, columnspan=2, sticky="e", padx=4, pady=2)

        self.save_and_exit_button = tk.Button(self, text="Save and Exit", command=self.save_and_exit, width=15, font=btn_font)
        self.save_and_exit_button.grid(row=row+1, column=col, columnspan=2, sticky="e", padx=4, pady=2)

        self.exit_button = tk.Button(self, text="Exit", command=self.exit_program, width=15, font=btn_font)
        self.exit_button.grid(row=row+2, column=col, columnspan=2, sticky="e", padx=4, pady=2)

    def save(self):
        new_env_values = {}
        for i, (key, value) in enumerate(self.env_values.items()):
            new_value = self.entries[i].get()
            new_env_values[key] = new_value
        with open(self.env_file_path, "w") as f:
            for key, value in new_env_values.items():
                f.write(f"{key}={value}\n")

    def save_and_exit(self):
        self.save()
        self.master.destroy()
        settings_path = os.path.join(fileRoot, "Examples", "Settings Main Menu.py")
        if getattr(sys, "frozen", False):
            settings_path = os.path.join(sys._MEIPASS, "Examples", "Settings Main Menu.py")
        subprocess.run(["python", settings_path])

    def exit_program(self):
        self.master.destroy()
        settings_path = os.path.join(fileRoot, "Examples", "Settings Main Menu.py")
        if getattr(sys, "frozen", False):
            settings_path = os.path.join(sys._MEIPASS, "Examples", "Settings Main Menu.py")
        subprocess.run(["python", settings_path])

parent_dir = og_dir
env_dir = os.path.join(parent_dir, "env", "twitch_settings.env")


if __name__ == "__main__":  
    root = tk.Tk()
    root.geometry("+{}+{}".format(root.winfo_screenwidth() // 2 - 200, root.winfo_screenheight() // 2 - 150))
    app = App(master=root, env_file_path=env_dir)
    app.mainloop()

