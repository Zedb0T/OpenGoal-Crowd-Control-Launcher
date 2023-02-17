import os
import tkinter as tk
from dotenv import dotenv_values
from EnvFileUpdater import EnvFileUpdater
import subprocess

class App(tk.Frame):
    def __init__(self, master=None, env_file_path=None):
        super().__init__(master)
        self.env_file_path = env_file_path
        self.env_values = dotenv_values(self.env_file_path)
        self.grid()
        self.create_widgets()
        master.title("Command Durations")

    def create_widgets(self):
        self.entries = []
        self.labels = []
        row = 0
        col = 0
        
        font = ('Helvetica', 10)
        btn_font = ('Helvetica', 10, 'bold')
        
        for key, value in self.env_values.items():
            label = tk.Label(self, text=key.replace("_dur", "").replace("ACTIVATE_MSG","Activation Message"), font=font)
            label.grid(row=row, column=col)
            self.labels.append(label)
            entry = tk.Entry(self, width=10)
            entry.insert(0, value)
            entry.grid(row=row, column=col + 1)
            self.entries.append(entry)
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
            new_value = self.entries[i].get()
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
env_dir = os.path.join(parent_dir, "env", "command_durations.env")

#Add fields if they do not exist
env_file_updater = EnvFileUpdater(env_dir)
env_file_updater.update(["ACTIVATE_MSG"], "#t")
env_file_updater.update(["protect_dur"], "60")
env_file_updater.update(["superjump_dur"], "60")
env_file_updater.update(["noboosteds_dur"], "180")
env_file_updater.update(["superboosted_dur"], "180")
env_file_updater.update(["fastjak_dur"], "90")
env_file_updater.update(["slowjak_dur"], "45")
env_file_updater.update(["slippery_dur"], "75")
env_file_updater.update(["pacifist_dur"], "60")
env_file_updater.update(["shortfall_dur"], "60")
env_file_updater.update(["ghostjak_dur"], "3")
env_file_updater.update(["freecam_dur"], "6")
env_file_updater.update(["noeco_dur"], "10")
env_file_updater.update(["rocketman_dur"], "5")
env_file_updater.update(["invertcam_dur"], "150")
env_file_updater.update(["dark_dur"], "30")
env_file_updater.update(["dax_dur"], "300")
env_file_updater.update(["smallnet_dur"], "10")
env_file_updater.update(["widefish_dur"], "4")
env_file_updater.update(["lowpoly_dur"], "300")
env_file_updater.update(["color_dur"], "90")
env_file_updater.update(["scale_dur"], "30")
env_file_updater.update(["widejak_dur"], "45")
env_file_updater.update(["flatjak_dur"], "45")
env_file_updater.update(["smalljak_dur"], "45")
env_file_updater.update(["bigjak_dur"], "45")
env_file_updater.update(["bighead_dur"], "45")
env_file_updater.update(["smallhead_dur"], "45")
env_file_updater.update(["bigfist_dur"], "45")
env_file_updater.update(["bigheadnpc_dur"], "45")
env_file_updater.update(["hugehead_dur"], "45")
env_file_updater.update(["mirror_dur"], "45")
env_file_updater.update(["notex_dur"], "45")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root, env_file_path=env_dir)
    app.mainloop()
