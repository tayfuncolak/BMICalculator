import tkinter

window = tkinter.Tk()
window.title("VKI Hesaplayıcı")
window.config(padx=100, pady=100)


def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()
    if weight == "" or height == "":
        result_label.config(text="Kilonuzu ve Boyunuzu girin!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Geçerli bir sayı girin!")


# ui
weight_input_label = tkinter.Label(text="Ağırlığınızı girin (kg)")
weight_input_label.pack()
weight_input = tkinter.Entry(width=10)
weight_input.pack()
height_input_label = tkinter.Label(text="Boyunuzu girin (cm)")
height_input_label.pack()
height_input = tkinter.Entry(width=10)
height_input.pack()
calculate_button = tkinter.Button(text="Hesapla", command=calculate_bmi)
calculate_button.pack()
result_label = tkinter.Label()
result_label.pack()


def write_result(bmi):
    result_string = f"Vücut Kitle İndeksiniz {round(bmi, 2)} Durumunuz: "
    if bmi <= 16:
        result_string += "Aşırı Zayıf!"
    elif 16 < bmi <= 17:
        result_string += "Orta Derecede Zayıf!"
    elif 17 < bmi <= 18.5:
        result_string += "Biraz Zayıf!"
    elif 18.5 < bmi <= 25:
        result_string += "Normal"
    elif 25 < bmi <= 30:
        result_string += "Şişman"
    elif 30 < bmi <= 35:
        result_string += "1. Derece Obez"
    elif 35 < bmi <= 40:
        result_string += "2. Derece Obez"
    else:
        result_string += "2. Derece Obez"
    return result_string


window.mainloop()
