import os
import utils
import tkinter as tk
from dotenv import dotenv_values


class App(tk.Frame):
    def __init__(self, master=None, env_file_path=None):
        super().__init__(master)
        self.env_file_path = env_file_path
        self.env_values = dotenv_values(self.env_file_path)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.entries = []
        self.labels = []
        row = 0
        col = 0
        for key, value in self.env_values.items():
            label = tk.Label(self, text=key)
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

        self.save_button = tk.Button(self, text="Save", command=self.save)
        self.save_button.grid(row=row + (int(len(self.env_values.items()))), column=col - 1, columnspan=2, sticky="e")
		
        self.save_and_exit_button = tk.Button(self, text="Save and Exit", command=self.save_and_exit)
        self.save_and_exit_button.grid(row=row+1, column=col, columnspan=2, sticky="e")

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


if __name__ == "__main__":
    env_file_path = r"C:\Users\Mike\Desktop\OpenGOAL\GitHub\OpenGoal-Crowd-Control-Launcher\env\twitch_settings.env"
    root = tk.Tk()
    app = App(master=root, env_file_path=env_file_path)
    app.mainloop()
