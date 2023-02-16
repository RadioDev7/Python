# Функция вывода информации
print("Привет мир")

myName = input("Your name - ") # ввод данных 
myAge = input("Hi %s, what about your age: " %(myName)) # ввод данных 

print("Hello World, my name is", myName, "and I am", myAge, "years old") # Вывод текста с 2 переменнами
print("Hello World, my name is %s and I am %s years old" %(myName, myAge)) # пример 2
print("Hello World, my name is {} and I am {} years old" .format(myName, myAge)) # пример 3

# Тройные ковычки
# Иногда нужно отобрать большой текст .
# Для этого используют тройные ковычки:
print("""
      Program python
      ver 1.54. os windows x64
      by User
      """)
      
# Экранированные символы
# Если нужно вывести спец символы. Например турбуляцию
# В этом случае нужно ввести символ \(+ Буква или цифра символа)
# Примеры (\)  \\ \' \" \a \b \f \n \r \t \v
print("TEST \\ TEST #1")
input("Нажни Enter для продолжения") #1

print("TEST \' TEST #2")
input("Нажни Enter для продолжения") #2

print("TEST \" TEST #3")
input("Нажни Enter для продолжения") #3

print("TEST \a TEST #4")
input("Нажни Enter для продолжения") #4

print("TEST \b TEST #5")
input("Нажни Enter для продолжения") #5

print("TEST \f TEST #6")
input("Нажни Enter для продолжения") #6

print("TEST \n TEST #7")
input("Нажни Enter для продолжения") #7

print("TEST \r TEST #8")
input("Нажни Enter для продолжения") #8

print("TEST \t TEST #9")
input("Нажни Enter для продолжения") #9

print("TEST \v TEST #10")
input("Нажни Enter для продолжения") #10