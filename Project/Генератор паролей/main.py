# By Артём Тарасов АС-21 ГПОУ КИТ
# Python project name - Генератор паролей
# Python version - 3.10.5 64bit windows, запущенная через VScode
import random # импортирование модуля случайных ответов
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' # список
# меню
number = input('Количество паролей?'+ "\n") # ввод данных 1
length = input('Длина пароля?'+ "\n") # ввод данных 2 
number = int(number) # переменная 1
length = int(length) # переменная 2
# система создания пароля
for n in range(number): # алгоритм
    password ='' # создание новой переменной
    for i in range(length): # функция генерациии длины пароля\
        password += random.choice(chars) # генерация 
    print(password) # вывод текста 
input("Нажмите кнопку чтобы выйти") # выход