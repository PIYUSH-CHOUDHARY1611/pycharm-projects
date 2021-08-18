import tkinter as tk
from tkinter import ttk
from tkinter .messagebox import showinfo
import random

win=tk.Tk()
win.title("Random Number Generator")
win.geometry("240x320")
win.configure(bg='black')
def play():
    randm_num = random.randint(1,6)
    number.config(text=f"Number is: {randm_num}")
    if randm_num ==6:
        showinfo("Congratulations","YOU WON!!")


number=tk.Label(win,text="",bg="yellow")
number.pack(pady=10)

play=tk.Button(win,text="Play",bg="red", fg="black",command=play)
play.pack(padx=50)

win.mainloop()