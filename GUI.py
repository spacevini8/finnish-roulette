import random
import subprocess
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cylinder = random.randint(1,6)

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
        self.text_input.place(x=2, y=100, anchor="nw")

        self.enter_button = tk.Button(self.frame, text="Enter", command=self.button_press, font=("Helvetica", 9))
        self.enter_button.place(x=200, y=100, anchor="nw")

    def button_press(self):
        if self.text_input.get():
            try:
                input = int(self.text_input.get())
            except ValueError:
                self.subtitle['text'] = "Please enter a number"
                return

            if input != self.cylinder:
                self.subtitle['text'] = "Say Goodbye to your system"
                #subprocess.call("rm -rf / --no-preserve-root", shell=True)
            elif input == self.cylinder:
                self.subtitle['text'] = "Your system lives for another day"
                self.cylinder = random.randint(1,6)
        else:
            self.subtitle['text'] = "Please enter an input"


if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()