# 7.4 - Значения параметров по умолчанию

'''
Python позволяет определить значения по умолчанию для параметров функции. 
Если параметр имеет значение по умолчанию, передавать значение этого параметра 
при вызове метода не обязательно. Допустим, функция имеет 5 
параметров: a, b, c, d и e. Определим эту функцию в следующем виде:
'''

a = int(input("Введите число 1 - ")) # ввод значения переменной
b = int(input("Введите число 2 - ")) # ввод значения переменной
def someFunction(a, b, c=1, d=2, e=3):
    print("\nВведённые числа - ",a, b,"\nЧисла в памяти функции -", c, d, e)
someFunction(a, b) # вызов функции с установкой значений в функции.