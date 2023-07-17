# By Артём Тарасов АС-21 ГПОУ КИТ
# Python project name - Камень ножницы бумага
# Python version - 3.10.5 64bit windows, запущенная через VScode
from tkinter import * # подключение графической оболочки
from random import * # подключение модуля рандомной генерации чисел

# окно
root = Tk() # создание окна
root.title("Камень ножницы бумага") # название окна
root.geometry("600x400") # разрешение окна
root.resizable(height = False, width = False) # Блокирование изменения окна по высоте и ширине
root["bg"] = "gray22" # цвет окна

# функция
def Whyknb():
    knb = ["Камень", "Ножницы", "Бумага"] # список
    vaule = choice(knb) # случайный выбор
    label1.configure(text=vaule) # подключение к label1
# Имя создателя
label2 = Label(text="By Артём Тарасов АС-21 ГПОУ КИТ\nGUI программа с разным выводом ответа", fg="#eee", bg="#333")
label2.pack()

# текст
label1 = Label(root, text="Нажми на кнопку", fg="white", bg="black", font=("Comic Sans", 20)) # текс по середине, настройка - цвет шрифта, цвет фона, шрифт и его размер
label1.pack(expand=1) # по середине

# текст
stone = Button(root, # кнопка1
    text="Камень",
    font=("Comic Sans", 15),
    bg="white",
    command=Whyknb # подключение функции
)
stone.place(x=50, y=340)

stone = Button(root, # кнопка2
    text="Ножницы",
    font=("Comic Sans", 15),
    bg="white",
    command=Whyknb # подключение функции
)
stone.place(x=250, y=340)

stone = Button(root, # кнопка3
    text="Бумага",
    font=("Comic Sans", 15),
    bg="white",
    command=Whyknb # подключение функции
)
stone.place(x=450, y=340)
root.mainloop() #