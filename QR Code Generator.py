import pyqrcode as df
from tkinter import *
from tkinter.filedialog import *

def generate():       #genrating QR code
    qr=entry.get()
    destination = askdirectory()
    filename= filename = asksaveasfilename(filetypes=[('PNG', '.png'),('SVG','.svg')
   ,('All files', '*')], defaultextension='.png')
    a=df.create(qr)
    a.png(filename)
#For GUI
root= Tk()
root.geometry('400x160')
root.title("QR Code Generator")

label = Label(root,text="Enter URL or Text",font=10).pack(fill=X,padx=15)
entry=Entry(root,width=100,font=10)
entry.pack(padx=15)
Button(root,text="Generate",command=generate,relief=RAISED,width=15,font=10).pack(pady=5)
Label(root,text="-Made by\n Rahul Raj Pandey ",font=('georgia',15)).pack(side=BOTTOM)

root.mainloop()










