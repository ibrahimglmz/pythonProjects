import tkinter
from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600, height=600)
window.config(padx=30 , pady=20)

label = Label(text="My Label")
label.config(bg="light blue")
label.config(fg="black")
label.config(padx=15, pady=15)
label.pack()


def button_clicked():
    print("deneme yazısı yazdir")


def spinbox_selected():
    print(my_spinbox.get())

my_spinbox = Spinbox(from_=0, to=50, command=spinbox_selected)
my_spinbox.pack()


def checkButton_Selected():
    my-checButton = Checkbutton(text="check", variable=)


button = Button(text="Button" , command=button_clicked)
button.config(padx=15, pady=15)
button.pack()



button_clicked()
tkinter.mainloop()