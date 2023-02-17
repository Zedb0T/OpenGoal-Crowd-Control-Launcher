import tkinter as tk
import subprocess

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = tk.Button(self, text="Twitch Settings", command=lambda: self.run_script(r"C:\Users\Mike\Desktop\OpenGOAL\GitHub\OpenGoal-Crowd-Control-Launcher\Examples\UI that reads twitch settings.py"))
        self.button1.grid(row=0, column=0)

        self.button2 = tk.Button(self, text="Enable Commands", command=lambda: self.run_script(r"C:\Users\Mike\Desktop\OpenGOAL\GitHub\OpenGoal-Crowd-Control-Launcher\Examples\UI that reads .env boolean checkmarks.py"))
        self.button2.grid(row=0, column=1)

        self.button3 = tk.Button(self, text="Command Cooldowns", command=lambda: self.run_script(r"C:\Users\Mike\Desktop\OpenGOAL\GitHub\OpenGoal-Crowd-Control-Launcher\Examples\UI that reads cooldowns.py"))
        self.button3.grid(row=1, column=0)

        self.button4 = tk.Button(self, text="Command Durations", command=lambda: self.run_script(r"C:\Users\Mike\Desktop\OpenGOAL\GitHub\OpenGoal-Crowd-Control-Launcher\Examples\UI that reads durations.py"))
        self.button4.grid(row=1, column=1)

    def run_script(self, script_path):
        subprocess.Popen(["python", script_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
