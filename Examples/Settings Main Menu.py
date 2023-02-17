import tkinter as tk
import subprocess

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

        self.button1 = tk.Button(self, text="Twitch Settings", command=lambda: self.run_script("Twitch Settings Menu.py"), width=20, font=font)
        self.button1.grid(row=0, column=0, padx=5, pady=5)

        self.button2 = tk.Button(self, text="Enabled Commands", command=lambda: self.run_script("Enabled Commands Menu.py"), width=20, font=font)
        self.button2.grid(row=0, column=1, padx=5, pady=5)

        self.button3 = tk.Button(self, text="Command Cooldowns", command=lambda: self.run_script("Command Cooldowns Menu.py"), width=20, font=font)
        self.button3.grid(row=1, column=0, padx=5, pady=5)

        self.button4 = tk.Button(self, text="Command Durations", command=lambda: self.run_script("Command Durations Menu.py"), width=20, font=font)
        self.button4.grid(row=1, column=1, padx=5, pady=5)


    def run_script(self, script_path):
        subprocess.Popen(["python", script_path])

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
