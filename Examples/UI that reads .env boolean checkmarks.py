import os
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
        self.checkboxes = []
        self.labels = []
        row = 0
        col = 0
        for key, value in self.env_values.items():
            label = tk.Label(self, text=key)
            label.grid(row=row, column=col)
            self.labels.append(label)
            var = tk.BooleanVar(value=value.lower() == 't')
            checkbox = tk.Checkbutton(self, variable=var)
            checkbox.grid(row=row, column=col + 1)
            self.checkboxes.append((var, checkbox))
            row += 1
            if row == (int(len(self.env_values.items()) / 4)):
                row = 0
                col += 2

        self.save_button = tk.Button(self, text="Save", command=self.save)
        self.save_button.grid(row=row, column=col, columnspan=2, sticky="e")

    def save(self):
        new_env_values = {}
        for i, (key, value) in enumerate(self.env_values.items()):
            new_value = 't' if self.checkboxes[i][0].get() else 'f'
            new_env_values[key] = new_value
        with open(self.env_file_path, "w") as f:
            for key, value in new_env_values.items():
                f.write(f"{key}={value}\n")


if __name__ == "__main__":
    env_file_path = r"C:\Users\Mike\Desktop\OpenGOAL\GitHub\OpenGoal-Crowd-Control-Launcher\env\command_enabled.env"
    root = tk.Tk()
    app = App(master=root, env_file_path=env_file_path)
    app.mainloop()
