from tkinter import *
from tkinter import messagebox
import base64
import os


def mainScreen():
    screen = Tk()
    screen.geometry("375x398")

    # icon
    imageIcon = PhotoImage(file="")
    screen.iconphoto(False, imageIcon)
    screen.title("PctApp")

    Label(
        text="Enter Secret key for encryption and decryption",
        fg="black",
        font=("calbri", 13),
    ).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="+").place(
        x=10, y=200
    )

    Button(text="ENCRYPT", height="2", width="23", bg="pink", fg="white", bd=0).place(
        x=10, y=250
    )
    Button(text="DECRYPT", height="2", width="23", bg="orange", fg="white", bd=0).place(
        x=200, y=250
    )
    Button(text="RESET", height="2", width="50", bg="yellow", fg="white", bd=0).place(
        x=10, y=250
    )

    screen.mainloop()


mainScreen()
