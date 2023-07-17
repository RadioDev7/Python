# By Артём Тарасов АС-21 ГПОУ КИТ
# Python project name - Калькулятор GUI
# Python version - 3.10.5 64bit windows, запущенная через VScode
import tkinter as tk # подключение графической оболочки
# работа кнопок
def add_digit(digit) : # функция цифр
    value = calc.get() 
    if value[0]=="0":
        value = value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)

def add_operation(operation) : # замена операций
    value = calc.get()
    if value [-1] in "+-/*":
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)

def make_digit_button(digit) : # функция команды кнопок
    return tk.Button(text=digit, bd=2, font=("Arial", 13), command=lambda : add_digit(digit))

def make_operation_button(operation) : # функция операции кнопок + - 
    return tk.Button(text=operation, bd=2, font=("Arial", 13), fg="blue", command=lambda : add_operation(operation))

def make_call_button(operation) : # вычисление
    return tk.Button(text=operation, bd=2, font=("Arial", 13), fg="blue", command=lambda : add_digit(operation))

# окно
wincalc = tk.Tk()
wincalc.geometry(f"240x275+100+200")
wincalc.resizable(height = False, width = False) # Блокирование изменения окна по высоте и ширине
wincalc["bg"] = "#eae4f0"
wincalc.title("Калькулятор")
# ввод
calc = tk.Entry(wincalc, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0,"0")
calc.grid(row=0, column=0, columnspan=4, stick="we", padx=2, pady=3)
# конпки
make_digit_button("1").grid(row=1, column=0, stick="wens", padx=3, pady=3)
make_digit_button("2").grid(row=1, column=1, stick="wens", padx=3, pady=3)
make_digit_button("3").grid(row=1, column=2, stick="wens", padx=3, pady=3)
make_digit_button("4").grid(row=2, column=0, stick="wens", padx=3, pady=3)
make_digit_button("5").grid(row=2, column=1, stick="wens", padx=3, pady=3)
make_digit_button("6").grid(row=2, column=2, stick="wens", padx=3, pady=3)
make_digit_button("7").grid(row=3, column=0, stick="wens", padx=3, pady=3)
make_digit_button("8").grid(row=3, column=1, stick="wens", padx=3, pady=3)
make_digit_button("9").grid(row=3, column=2, stick="wens", padx=3, pady=3)
make_digit_button("0").grid(row=4, column=0, stick="wens", padx=3, pady=3)

make_operation_button("+").grid(row=1, column=3, stick="wens", padx=3, pady=3)
make_operation_button("-").grid(row=2, column=3, stick="wens", padx=3, pady=3)
make_operation_button("/").grid(row=3, column=3, stick="wens", padx=3, pady=3)
make_operation_button("*").grid(row=4, column=3, stick="wens", padx=3, pady=3)

make_call_button("=").grid(row=4, column=1, stick="wens", padx=3, pady=3)
# настройка GUI
wincalc.grid_columnconfigure(0,minsize=60)
wincalc.grid_columnconfigure(1,minsize=60)
wincalc.grid_columnconfigure(2,minsize=60)
wincalc.grid_columnconfigure(3,minsize=60)

wincalc.grid_rowconfigure(1,minsize=60)
wincalc.grid_rowconfigure(2,minsize=60)
wincalc.grid_rowconfigure(3,minsize=60)
wincalc.grid_rowconfigure(4,minsize=60)

wincalc.mainloop ()
