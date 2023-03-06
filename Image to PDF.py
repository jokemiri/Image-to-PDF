import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Color Finder")
root.geometry("800x470+100+100")
root.configure(bg="#1e81b0")
root.resizable(False, False)



def select_image():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File', filetype=(('PNG file','*.png'),('JPG file','*.jpg'),('ALL files','*.txt')))

    global img

    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=310, height=270)
    # lbl.image=img

def convert():
    image=img.convert("RGB")
    image.save("PDF File.pdf")

#window_icon
window_icon = PhotoImage(file="icon.png")
root.iconphoto(False, window_icon)

Label(root, width=120, height=10, bg="#52bbd8").pack()

#frame
frame = Frame(root, width=750, height=420, bg='#d6e9ee')
frame.place(x=25, y=10)

logo = PhotoImage(file='logo.png')
Label(frame, image=logo, bg='#d6e9ee').place(x=10, y=10)

Label(frame, text='Color Finder', font='Calibri 18 bold', bg='#d6e9ee').place(x=100, y=20)

#image selector
image_selector = Frame(frame, width=340, height=350, bg='white', border=1)
image_selector.place(x=380,y=58)

frame2 = Frame(image_selector, bd=3, bg='black', width=320, height=280, relief=GROOVE)
frame2.place(x=10, y=10)

lbl=Label(frame2, bg='black')
lbl.place(x=0, y=0)

Button(image_selector, text='Select Image', width=12, height=1, font='Calibri 14 bold', command=select_image).place(x=10, y=300)
Button(image_selector, text='Convert', width=12, height=1, font='Calibri 14 bold', command=convert).place(x=200, y=300)


root.mainloop()