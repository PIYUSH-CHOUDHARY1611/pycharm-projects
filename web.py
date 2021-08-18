import tkinter as tk
from tkinter import *
import time
import webbrowser

win = tk.Tk()
win.title("WebBrowser")
win.geometry("480x480")
win.configure(bg='red')

def digital_clock():
    time1= time.strftime("%H:%M:%S")
    current_time.config(text=time1)
    current_time.after(250,digital_clock)

def google():
    webbrowser.open("www.google.com")


def youtube():
    webbrowser.open("www.youtube.com")


def twitter():
    webbrowser.open("www.twitter.com")


def facebook():
    webbrowser.open("www.facebook.com")


def search():
    url = entry.get()
    webbrowser.open(url)


# igoogle = PhotoImage(file="google.png")
google = tk.Button(win, text='google',width=10 ,font=("Algerian", 25, "bold"), command=google)
google.grid(row=2, column=0,pady=10)

# iyoutube = PhotoImage(file="youtube.png")
youtube = tk.Button(win, text="youtube",width=10, font=("Algerian", 20, "bold"), command=youtube)
youtube.grid(row=2, column=1,pady=10)

# ifacebook = PhotoImage(file="facebook.png")
facebook = tk.Button(win, text="facebook", width=10,font=("Algerian", 20, "bold"), command=facebook)
facebook.grid(row=3, column=0,pady=10)

# itwitter = PhotoImage(file="download.png")
twitter = tk.Button(win, text="twitter",width=10, font=('Algerian', 25, "bold"), command=twitter)
twitter.grid(row=3, column=1,pady=10)

entry = Entry(win, width=20)
entry.grid(row=0, column=0,padx=10)

button = Button(win, text="Search", font=("Algerian", 10, "bold"), command=search)
button.grid(row=1,padx=10,pady=10)

current_time= Label(win,font=("tim",25,'bold'),bg='yellow')
current_time.grid(row=4,column=0)
digital_clock()



win.mainloop()
