# Форматирование строк с помощью format()

# При использовании метода format() заполнители %s, 
# %f или %d не применяются. Вместо этого используются 
# фигурные скобки {}, например:

message = 'The price of this {0:s} laptop is {1:d}  USD and the exchange rate is {2:4.2f} USD to 1 EUR'. format('Apple', 1299, 1.235235245)
print(message)

# {2:4.2f} где 2 - id скобок, 4.2f - функция десятичных чисел

# Пример 
message1 = '{0} is easier than {1}'.format('Python', 'Java')
message2 = '{1} is easier than {0}'.format('Python', 'Java')
message3 = '{:10.2f} and {:d}'.format(1.234234234, 12)
message4 = '{}'.format(1.234234234)
print (message1)
# Получим 'Python is easier than Java'
print (message2)
# Получим 'Java is easier than Python'
print (message3)
print (message4) # форматирование не выполняется

