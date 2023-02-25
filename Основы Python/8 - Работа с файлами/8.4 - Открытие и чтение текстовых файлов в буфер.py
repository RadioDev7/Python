# 8.4 - Открытие и чтение текстовых файлов в буфер.py
inputFile = open ('number.txt', 'r') # открытие файла
outputFile = open ('bufer_obmena.txt', 'w') # открытие файла + удаленние данных
msg = inputFile.read(10) # чтение файла по 10 байт.
while len(msg): # создание цикла
    outputFile.write(msg) # запись информации в bufer_obmena
    msg = inputFile.read(10) # чтение файла по 10 байт.
inputFile.close() # закрытие файла
outputFile.close() # закрытие файла

f = open('bufer_obmena.txt', 'r', encoding='UTF-8') # Открытие файла
line1 = f.readline() # чтение 1 строки + \n
line2 = f.readline() # чтение 2 строки + \n
print(line1) # вывод 1 строки
print(line2) # вывод 2 строки
f.close() # закрытие файла 