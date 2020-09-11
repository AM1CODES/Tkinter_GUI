import random
import string
from tkinter import *


win = Tk()
win.geometry("200x100") #setting the geometry of the window
win.title("Password Generator") #title of the GUI Window
win.iconbitmap(r'C:\Users\deepa\Downloads\Icons8-Ios7-Logos-Register-Editor.ico') #icon for the gui window


def randomPassword(): #method that generates random password
    pass_char = string.ascii_letters + string.digits + string.punctuation #combining letters,digits,punctuation marks etc.
    password = random.choice(string.ascii_lowercase) #generating lowercase characters
    password += random.choice(string.ascii_uppercase) #generatinng upper case characters and cmbing it with the password
    password += random.choice(string.digits) #generating digits
    password += random.choice(string.punctuation) #generating punctuation marks

    for i in range(6):
        password += random.choice(pass_char) #randomly  generating a password of length of 6 characters

    passwordList = list(password) #storing the characters in a list format
    random.SystemRandom().shuffle(passwordList) #shuffling the characters of the list
    password = ''.join(passwordList) #combining everything to generate the password
    print(password)
    label1 = Label(win, text=f"Generated Password: {password}", bg="red")
    label1.pack()


win_button = Button(win,text = "Generate Pass",bg = 'black', fg ='red',command = randomPassword )
win_button.pack()

win.mainloop()