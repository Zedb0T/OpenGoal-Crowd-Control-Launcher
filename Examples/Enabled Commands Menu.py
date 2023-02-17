import os
import tkinter as tk
from dotenv import dotenv_values
import subprocess

class App(tk.Frame):
    def __init__(self, master=None, env_file_path=None):
        super().__init__(master)
        self.env_file_path = env_file_path
        self.env_values = dotenv_values(self.env_file_path)
        self.grid()
        self.create_widgets()
        master.title("Enabled Commands")

    def create_widgets(self):
        self.checkboxes = []
        self.labels = []
        row = 0
        col = 0
        
        font = ('Helvetica', 10)
        btn_font = ('Helvetica', 10, 'bold')
        
        for key, value in self.env_values.items():
            label = tk.Label(self, text=key, font=font)
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
                
        self.save_button = tk.Button(self, text="Save", command=self.save, width=15, font=btn_font)
        self.save_button.grid(row=row, column=col, columnspan=2, sticky="e", padx=4, pady=2)

        self.save_and_exit_button = tk.Button(self, text="Save and Exit", command=self.save_and_exit, width=15, font=btn_font)
        self.save_and_exit_button.grid(row=row+1, column=col, columnspan=2, sticky="e", padx=4, pady=2)
		
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_program, width=15, font=btn_font)
        self.exit_button.grid(row=row+2, column=col, columnspan=2, sticky="e", padx=4, pady=2)


    def save(self):
        new_env_values = {}
        for i, (key, value) in enumerate(self.env_values.items()):
            new_value = 't' if self.checkboxes[i][0].get() else 'f'
            new_env_values[key] = new_value
        with open(self.env_file_path, "w") as f:
            for key, value in new_env_values.items():
                f.write(f"{key}={value}\n")

    def save_and_exit(self):
       self.save()
       self.master.destroy()
       subprocess.run(["python", "Settings Main Menu.py"])
       
    def exit_program(self):
        self.master.destroy()
        subprocess.run(["python", "Settings Main Menu.py"])
        
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
env_dir = os.path.join(parent_dir, "env", "command_enabled.env")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root, env_file_path=env_dir)
    app.mainloop()
