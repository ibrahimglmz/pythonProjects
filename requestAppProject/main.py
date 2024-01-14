from  tkinter import *
from tkinter import  messagebox
import  requests
from bs4 import BeautifulSoup

screen = Tk()
screen.title("Hava Durumu Uygulaması")
screen.minsize(width=350,height=650)
screen.config(padx=20,pady=20)
TEXTT = ""


sehriyazEntry = Entry(width=20)
sehriyazEntry.pack()

havaDurumGösterButon = Button(text="Hava Nasıl ? ")
havaDurumGösterButon.pack()

outputLabel = Label(width=20,  height=20, background="light blue",text=TEXTT)
outputLabel.pack()


screen.mainloop()