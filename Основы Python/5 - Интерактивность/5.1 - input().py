# Функция ввода информации

myName = input("Your name - ") # ввод данных 
print(myName) # вывод данных

# также можно написать сокращённо
myAge = input("Hi %s, what about your age: " %(myName))

# или так
myAge = input("Hi {}, what about your age: ".format(myName))

# вывод
print("Your Age {}, Your name {}".format(myName, myAge))

