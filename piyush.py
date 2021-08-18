import tkinter as tk
from gtts import gTTS
from playsound import playsound
win=tk.Tk()
win.title("text_to_speech")
win.geometry("200x100")

def text_to_speech():
    text=entry.get()
    speech=gTTS(text=text,lang="en")
    speech.save(r'C:\Users\DRAGON RIDER\Downloads\speech.mp3')
    playsound(r'C:\Users\DRAGON RIDER\Downloads\speech.mp3')


label=tk.Label(win,text="Enter Here",font="Algerian")
label.grid(row=0,column=0)

entry=tk.Entry(win)
entry.grid(row=1,column=0)
button=tk.Button(win,text="go",command=text_to_speech)
button.grid(row=1,column=1)

win.mainloop()