import tkinter as tk

cal = tk.Tk()
cal.title("Calculator")


def click(number):
    global oprator
    oprator = oprator + str(number)
    variable.set(oprator)


def clear():
    global oprator
    oprator = " "
    variable.set(oprator)


def sum():
    global oprator
    oprator = str(eval(oprator))
    variable.set(oprator)


oprator = " "
variable = tk.StringVar()

display = tk.Entry(cal, font=("Algerian", 20, "bold"), bd=25, textvariable=variable, justify="right")
display.grid(columnspan=5)

button7 = tk.Button(cal, text="7", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click(7))
button7.grid(row=1, column=0)

button8 = tk.Button(cal, text="8", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click(8))
button8.grid(row=1, column=1)

button9 = tk.Button(cal, text="9", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click(9))
button9.grid(row=1, column=2)

button4 = tk.Button(cal, text="4", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click(4))
button4.grid(row=2, column=0)

button5 = tk.Button(cal, text="5", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click(5))
button5.grid(row=2, column=1)

button6 = tk.Button(cal, text="6", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click(6))
button6.grid(row=2, column=2)

button1 = tk.Button(cal, text="1", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click(1))
button1.grid(row=3, column=0)

button2 = tk.Button(cal, text="2", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click(2))
button2.grid(row=3, column=1)

button3 = tk.Button(cal, text="3", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click(3))
button3.grid(row=3, column=2)

button0 = tk.Button(cal, text="0", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click(0))
button0.grid(row=4, column=0)

buttonpoint = tk.Button(cal, text=".", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click("."))
buttonpoint.grid(row=4, column=1)

buttonclear = tk.Button(cal, text="C", font=("Algerian", 20, "bold"), bd=20, padx=10, command=clear)
buttonclear.grid(row=4, column=2)

buttonplus = tk.Button(cal, text="+", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click("+"))
buttonplus.grid(row=1, column=3)

buttonminus = tk.Button(cal, text="-", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click("-"))
buttonminus.grid(row=2, column=3)

buttonproduct = tk.Button(cal, text="*", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click("*"))
buttonproduct.grid(row=3, column=3)

buttondiv = tk.Button(cal, text="/", font=("Algerian", 20, "bold"), bd=20, padx=10, command=lambda: click("/"))
buttondiv.grid(row=4, column=3)

buttonequals = tk.Button(cal, text="=", font=("Algerian", 20, "bold"), bd=20, padx=100, command=sum)
buttonequals.grid(row=5, columnspan=6)
cal.mainloop()
