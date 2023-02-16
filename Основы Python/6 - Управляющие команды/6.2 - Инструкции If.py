# Инструкция if нужна для выполнение задач с определенным 
# значением, задача выбирается пользователемю
# -----------------------------------------------------
# Конструкция if выглядит так:
# if выполняется условие 1:
# выполнить A
# elif выполняется условие 2:
# выполнить B
# else:
# выполнить E

# Пример программы
userInput = input('Enter 1 or 2: ');
if userInput == "1":
	print("Hello World");
	print("How are you?");
elif userInput == "2":
	print("Python Rocks!");
	print("I love Python");
else:	
	print("error");