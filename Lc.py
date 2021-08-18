import tkinter as tk

from tkinter.messagebox import showinfo

win = tk.Tk()
win.title("Friendship Calculator")
win.configure(bg="orange")
win.geometry("640x640")
var = tk.StringVar()
var1=tk.StringVar()


label1 = tk.Label(win, text="Enter your name", font=("algerian", 10, "bold"))
label1.grid(row=6, column=0, padx=1, pady=10, sticky='W')

entry1 = tk.Entry(win, textvariable=var, font=("algerian", 10, "bold"))
entry1.grid(row=6, column=1, padx=0, pady=0)

label2 = tk.Label(win, text="Enter your Friends name", font=("algerian", 10, "bold"))
label2.grid(row=8, column=0, sticky="W", padx=1, pady=0)

entry2 = tk.Entry(win, textvariable=var1, font=("algerian", 10, "bold"))
entry2.grid(row=8, column=1, sticky="W", padx=0, pady=0)
name1=var.get()
name2=var1.get()
names=name1+name2
alphabet = 'qwtypdghjklzxcvbm'
score = 0
for char in name2:
    if char in 'aeiou':
     score += 5
     if char in 'friends':
       score += 10
     if char in alphabet:
        score += alphabet.find(char)
     else:
        score += 0



label3 = tk.Label(win, text=your score is, font=("algerian", 10, "bold"))
label3.grid(row=12, column=0, sticky="W", padx=1, pady=0)




win.mainloop()
