# 6.8 - TRY/EXCEPT
# оператор try/except. Он контролирует работу программы при возникновении 
# ошибки

# Программа 1
try:
    answer = 12/6
    print (answer)
except:
    print ("Ошибка!")

# Программа 2
try:
    answer = 12/0
    print (answer)
except:
    print ("Ошибка!")
    
try:
    userInput1 = int(input("Please enter a number: "))
    userInput2 = int(input("Please enter another number: "))
    answer = userInput1/userInput2
    print ("The answer is ", answer)
    myFile = open("missing.txt", 'r') # если файла нет, то программа выдаёт error
except ValueError:
    print ("Error: Вводимые цифры не правильные")
except ZeroDivisionError:
    print ("Error: На ноль делить нельзя")
except Exception as e:
    print ("Unknown error: ", e)

# Другие типы распространенных ошибок в Python

# IOError:
# Операция ввода/вывода (например, встроенная функция open()) завершилась
# неудачей по причине, связанной с вводом/выводом, — например, «файл не найден».

# ImportError:
# Команда import не находит определение модуля.

# IndexError:
# Последовательность (строка, список, кортеж) выходит 
# за пределы диапазона.

# KeyError:
# Ключ словаря не найден.

# NameError:
# Локальное или глобальное имя не найдено

# TypeError:
# Операция или функция применяется к объекту непод-ходящего типа.

# Полный список типов ошибок в Python см. по адресу: 
# https://docs.python.org/3/library/exceptions.html

# Дополнительное
try:
	a = int(input())
	b = int(input())
	c = a/b
	print(c)
except ZeroDivisionError as e:
	print(e)
except ValueError as e:
	print(e)