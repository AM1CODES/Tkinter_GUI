import tkinter as tk
from PIL import Image

win = tk.Tk()
win.title("Image converter")
def converter():
    open_image = Image.open(r'C:\Users\deepa\Pictures\Snapshot - 1.png')
    bw_image = open_image.convert("L")
    bw_image.show()

button = tk.Button(win,text = "Convert",command = converter)
button.grid(row=1, column=1)


win.mainloop()
