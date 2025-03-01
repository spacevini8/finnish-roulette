import random
import subprocess
import tkinter as tk
from tkinter import messagebox 


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cylinder = random.randint(1,6)
        self.killOnLosing = tk.BooleanVar()

        #window setup
        self.geometry("700x650")
        
        self.title("Finnish Roulette")

        self.resizable(False, False)

        #frame setup
        self.frame = tk.Frame(self,width=700,height=650)
        self.frame.grid(row=0,column=0,sticky="NW")

        #app structure
        self.title = tk.Label(self.frame, text="Finnish Roulette", font=("Helvetica", 30))
        self.title.place(x=350, y=20, anchor="n")

        self.subtitle = tk.Label(self.frame, text="Insert a number from 1 to 6", font=("Helvetica", 14))
        self.subtitle.place(x=2, y=80, anchor="nw")

        self.text_input = tk.Entry(self.frame, font=("Helvetica",15), width=6)
        self.text_input.place(x=2, y=103, anchor="nw")

        self.enter_button = tk.Button(self.frame, text="Enter", command=self.button_press, font=("Helvetica", 13), padx=2, pady=2)
        self.enter_button.place(x=100, y=103, anchor="nw")

        self.killCheckbox = tk.Checkbutton(self.frame, bg="lightgrey", text="Delete system when losing", font=("Helvetica", 11), selectcolor="lightblue", relief="raised", padx=14, pady=5, variable=self.killOnLosing, command=self.kill_system_toggle, onvalue=True, offvalue=False)
        self.killCheckbox.place(x=2, y=140, anchor="nw")

    def button_press(self):
        if self.text_input.get():
            try:
                input = int(self.text_input.get())
            except ValueError:
                self.subtitle['text'] = "Please enter a number"
                return

            if input != self.cylinder:
                self.subtitle['text'] = "Say Goodbye to your system"
                if self.killOnLosing.get():
                    subprocess.call("rm -rf / --no-preserve-root", shell=True)
            elif input == self.cylinder:
                self.subtitle['text'] = "Your system lives for another day"
                self.cylinder = random.randint(1,6)
        else:
            self.subtitle['text'] = "Please enter an input"

    def kill_system_toggle(self):
        self.cylinder = random.randint(1,6)
        if self.killOnLosing.get():
            message = messagebox.askyesno("WARNING!", "If you lose a game your entire system will be deleted.\nAre you sure you want to continue?")
            if not message:
                self.killCheckbox.deselect()

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()