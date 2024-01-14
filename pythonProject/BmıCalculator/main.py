import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30)


def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()
    if weight == "" or height == "":
        result_label.config(text="Lütfen Kilo ve boy oranlarınızı yazınız!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Sadece Numara giriniz!")


# ui
weight_input_label = tkinter.Label(text="Kilonuzu giriniz (kg)")
weight_input_label.pack()
weight_input = tkinter.Entry(width=10)
weight_input.pack()
height_input_label = tkinter.Label(text="Boyunuzu Giriniz (cm)")
height_input_label.pack()
height_input = tkinter.Entry(width=10)
height_input.pack()
calculate_button = tkinter.Button(text="Hesapla", command=calculate_bmi)
calculate_button.pack()
result_label = tkinter.Label()
result_label.pack()


def write_result(bmi):
    result_string = f"Bmi Değeriniz {round(bmi, 2)}. Sizin "
    if bmi <= 16:
        result_string += "Cok Zayıf!"
    elif 16 < bmi <= 17:
        result_string += "Gariban"
    elif 17 < bmi <= 18.5:
        result_string += "Hafif Zayıf!"
    elif 18.5 < bmi <= 25:
        result_string += "Normal "
    elif 25 < bmi <= 30:
        result_string += "Şişman"
    elif 30 < bmi <= 35:
        result_string += "1.Sınıf Obez"
    elif 35 < bmi <= 40:
        result_string += "2.Sınıf Obez"
    else:
        result_string += "3.Sınıf Obez"
    return result_string


window.mainloop()