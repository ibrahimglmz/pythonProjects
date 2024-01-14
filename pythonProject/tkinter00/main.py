import tkinter
window = tkinter.Tk()
window.title("Python TkInter App")
window.minsize(250 , 250)

def clicked_button():
    user_input = my_entry.get()
    print(user_input)


my_label = tkinter.Label(text="Deneme Başlık")
my_label.config(bg="light blue", fg="red")
my_label.pack()


my_button = tkinter.Button(text="Button", command=clicked_button)
my_button.pack()


my_entry = tkinter.Entry(width=20)
my_entry.pack()



clicked_button()
tkinter.mainloop()