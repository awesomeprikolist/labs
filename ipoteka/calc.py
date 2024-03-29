import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Ипотечный калькулятор")

label1 = tk.Label(window, text="Стоимость недвижимости:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

label2 = tk.Label(window, text="Первоначальный взнос:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

label3 = tk.Label(window, text="Срок кредита:")
label3.grid(row=2, column=0)
scale1 = tk.Scale(window, from_=1, to=30, orient=tk.HORIZONTAL)
scale1.grid(row=2, column=1)

label4 = tk.Label(window, text="Процентная ставка:")
label4.grid(row=3, column=0)
label5 = tk.Label(window, text="6.4%")
label5.grid(row=3, column=1)

label6 = tk.Label(window, text="Тип кредита:")
label6.grid(row=4, column=0)
var1 = tk.IntVar()
check1 = tk.Checkbutton(window, text="Льготный", variable=var1)
check1.grid(row=4, column=1)

label7 = tk.Label(window, text="Ежемесячный платеж:")
label7.grid(row=5, column=0)
entry3 = tk.Entry(window)
entry3.grid(row=5, column=1)


def calculate():
    price = float(entry1.get())
    vznos = float(entry2.get())
    srok = scale1.get()
    stavka = 6.4
    credit_type = var1.get()

    if price <= 0 or vznos < 0.15 * price or srok <= 0:
        entry3.delete(0, tk.END)
        entry3.insert(0, "Неверные данные")

    credit_sum = price - vznos
    monthly_stavka = stavka / 12 / 100
    number_of_payments = srok * 12
    monthly_payment = credit_sum * (monthly_stavka * (1 + monthly_stavka) ** number_of_payments) / (
            (1 + monthly_stavka) ** number_of_payments - 1)

    if credit_type == 1:
        monthly_payment = monthly_payment * 0.9

    monthly_payment = round(monthly_payment)

    entry3.delete(0, tk.END)
    entry3.insert(0, f"{monthly_payment} руб.")


button = tk.Button(window, text="Рассчитать", command=calculate)
button.grid(row=6, column=0, columnspan=2)

window.mainloop()
