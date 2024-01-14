from  tkinter import *
from tkinter import messagebox
import base64
# notları kriptolayarak saklamaya yarayan not kayıt uygulaması
def encode(key,clear):
    enc =[]
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()



def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def decrytp_notes():
    message_encrypt = input_Text.get("1.0", END)
    master_secret = master_secret_Input.get()

    if len(message_encrypt) == 0 or len(master_secret) == 0:
        messagebox.showerror(title="ERROR", message="Lütfen Bilgi Giriniz !")
    else:
        try:
            decrytpe_messege = decode(master_secret, message_encrypt)
            input_Text.delete("1.0", END)
            input_Text.insert("1.0", decrytpe_messege)
        except:
            messagebox.showinfo(title="ERROR", message="bozuldu qw !")

FONT = ("Verdena",20,"normal")
window = Tk()
window.title("Secret Notes")
window.minsize(width=350, height=650)
window.config(padx=20 ,pady=20)


def save_and_encrypt_notes():
    tittle = tittle_Entry.get()
    message = input_Text.get("1.0", END)
    master_secret = master_secret_Input.get()

    if len(tittle) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showerror(title="ERROR", message="Lütfen Bilgi Giriniz !")
    else:
        message_encrypted = encode(master_secret, message)
        try:
            with open("myscreet.txt", "a") as data_file:
                 data_file.write(f"\n{tittle}\n{message_encrypted}")
        except FileExistsError:
            with open("myscreet.txt", "w") as data_file:
                data_file.write(f"\n{tittle}\n{message_encrypted}")
        finally:
            tittle_Entry.delete(0,END)
            master_secret_Input.delete(0,END)
            input_Text.delete("1.0",END)






photo = PhotoImage(file="download.png")
photo_label = Label(window, image=photo)
photo_label.pack()


tittle = Label(window, text="Enter Your Title", font=FONT)
tittle.pack()

tittle_Entry = Entry(width=20)
tittle_Entry.pack()

input_label = Label(text="Enter Your Secret", font=FONT)
input_label.pack()
input_Text = Text(width=50,height=25)
input_Text.pack()

master_secret_label = Label(text="Enter master Key", font=FONT)
master_secret_label.pack()

master_secret_Input = Entry(width=20)
master_secret_Input.pack()

save_button = Button(text="Save & Encrypt", command=save_and_encrypt_notes)
save_button.pack()

decryption_button = Button(text="Decrypt", command=decrytp_notes)
decryption_button.pack()




window.mainloop()