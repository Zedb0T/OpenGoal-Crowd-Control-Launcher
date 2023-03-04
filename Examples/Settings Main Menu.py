import os
import sys
import tkinter as tk
from tkinter import ttk
import subprocess

global run_Type

def get_parent_directory():
    run_Type = ""
    if getattr(sys, 'frozen', False):
        if "Release" in sys.executable:
            run_Type = "ReleaseDIR"
            return os.path.dirname(os.path.dirname(sys.executable)), run_Type
        else:
            run_Type = "AppdataDIR"
            return os.path.abspath(os.path.join(os.path.dirname(sys.executable), os.pardir)), run_Type
    else:
        run_Type= "ScriptDIR"
        return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), run_Type
    
parent_dir, run_Type = get_parent_directory()


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        master.title("Main Settings")

    def create_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        font = ('Helvetica', 10, "bold")

        self.button1 = ttk.Button(self, text="Twitch Settings", command=self.run_TwitchSettings, width=20)
        self.button1.grid(row=0, column=0, padx=5, pady=5)

        self.button2 = ttk.Button(self, text="Enabled Commands", command=self.run_EnabledCommands, width=20)
        self.button2.grid(row=0, column=1, padx=5, pady=5)

        self.button3 = ttk.Button(self, text="Command Cooldowns", command=self.run_CommandCooldowns, width=20)
        self.button3.grid(row=1, column=0, padx=5, pady=5)

        self.button4 = ttk.Button(self, text="Command Durations", command=self.run_CommandDurations, width=20)
        self.button4.grid(row=1, column=1, padx=5, pady=5)
        
        self.button5 = tk.Button(self, text="Exit", command=self.exit_program, width=10, font=font)
        self.button5.grid(row=2, column=1, padx=5, pady=5)


    def run_TwitchSettings(self):
        
        if run_Type == "ReleaseDIR":
            self.master.destroy()
            settings_path = os.path.join(parent_dir, "bin", "Twitch Settings Menu.exe")
            print(settings_path)
            subprocess.run([settings_path])
            
        if run_Type == "AppdataDIR":
            #TODO
            self.master.destroy()
        
        if run_Type == "ScriptDIR":
            self.master.destroy()
            settings_path = os.path.join(parent_dir, "Examples", "Twitch Settings Menu.py")
            print(settings_path)
            subprocess.run(["python", settings_path])
    
    def run_EnabledCommands(self):
        
        if run_Type == "ReleaseDIR":
            self.master.destroy()
            settings_path = os.path.join(parent_dir, "bin", "Enabled Commands Menu.exe")
            print(settings_path)
            subprocess.run([settings_path])
            
        if run_Type == "AppdataDIR":
            #TODO
            self.master.destroy()
        
        if run_Type == "ScriptDIR":
            self.master.destroy()
            settings_path = os.path.join(parent_dir, "Examples", "Enabled Commands Menu.py")
            print(settings_path)
            subprocess.run(["python", settings_path])

    def run_CommandCooldowns(self):
        
        if run_Type == "ReleaseDIR":
            self.master.destroy()
            settings_path = os.path.join(parent_dir, "bin", "Command Cooldowns menu.exe")
            print(settings_path)
            subprocess.run([settings_path])
            
        if run_Type == "AppdataDIR":
            #TODO
            self.master.destroy()
        
        if run_Type == "ScriptDIR":
            self.master.destroy()
            settings_path = os.path.join(parent_dir, "Examples", "Command Cooldowns menu.py")
            print(settings_path)
            subprocess.run(["python", settings_path])
    
    def run_CommandDurations(self):
        
        if run_Type == "ReleaseDIR":
            self.master.destroy()
            settings_path = os.path.join(parent_dir, "bin", "Command Durations menu.exe")
            print(settings_path)
            subprocess.run([settings_path])
            
        if run_Type == "AppdataDIR":
            #TODO
            self.master.destroy()
        
        if run_Type == "ScriptDIR":
            self.master.destroy()
            settings_path = os.path.join(parent_dir, "Examples", "Command Durations menu.py")
            print(settings_path)
            subprocess.run(["python", settings_path])

    def exit_program(self):

        if run_Type == "ReleaseDIR":
            self.master.destroy()
            settings_path = os.path.join(parent_dir, "bin", "Crowd Control Main Menu.exe")
            print(settings_path)
            subprocess.run([settings_path])
            
        if run_Type == "AppdataDIR":
            #TODO
            self.master.destroy()
        
        if run_Type == "ScriptDIR":
            self.master.destroy()
            settings_path = os.path.join(parent_dir, "Examples", "Crowd Control Main Menu.py")
            print(settings_path)
            subprocess.run(["python", settings_path])

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("+{}+{}".format(root.winfo_screenwidth() // 2 - 200, root.winfo_screenheight() // 2 - 150))
    app = App(master=root)
    app.mainloop()
