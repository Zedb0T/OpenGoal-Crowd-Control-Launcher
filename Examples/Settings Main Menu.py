import os
import sys
import tkinter as tk
import subprocess

if getattr(sys, "frozen", False):
    # If we are a pyinstaller exe get the path of this file, not python
    fileRoot = sys._MEIPASS
else:
    # if we are running the .py directly use this path
    fileRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) 

og_dir = os.path.join(os.getenv("APPDATA"), "OpenGOAL-CrowdControl","")


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
        
        self.button5 = tk.Button(self, text="Exit", command=self.exit_program, width=10, font=font)
        self.button5.grid(row=2, column=1, padx=5, pady=5)

    def run_script(self, script_path):
        self.master.destroy()
        if getattr(sys, 'frozen', False):
            script_path = os.path.join(sys._MEIPASS,  os.path.basename(script_path))
            # Get the temporary directory of the PyInstaller executable
            temp_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(sys.argv[0])))
            # Look for directories within the temporary directory
            examples_dir = os.path.join(temp_dir)
            print("AHHHHH " + examples_dir)
        else:
            examples_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
            print("AHHHHH " +examples_dir)
        subprocess.run(["python", script_path], cwd=examples_dir)

        
    def exit_program(self):
        self.master.destroy()
        main_menu_path = os.path.join(fileRoot, "Examples", "Crowd Control Main Menu.py")
        if getattr(sys, "frozen", False):
            main_menu_path = os.path.join(sys._MEIPASS, "Examples", "Crowd Control Main Menu.py")
        subprocess.run(["python", main_menu_path])

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("+{}+{}".format(root.winfo_screenwidth() // 2 - 200, root.winfo_screenheight() // 2 - 150))
    app = App(master=root)
    app.mainloop()
