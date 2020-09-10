import tkinter as tk
from gtts import gTTS
from playsound import playsound

win = tk.Tk()
win.title("Text To Speech")
win.geometry("200x70")


def texts():
    text = entry.get()
    speech = gTTS(text=text, lang="en")
    speech.save(r'C:\Users\deepa\Downloads\speech.mp3')
    playsound(r'C:\Users\deepa\Downloads\speech.mp3')


label = tk.Label(win, text="Enter the text :")
label.grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=1, column=0)

button = tk.Button(win, text="Covert", command=texts)
button.grid(row=1, column=1)

win.mainloop()
