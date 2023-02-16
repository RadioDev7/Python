# Форматирование строк с помощью оператора %

brand = 'Apple'
exchangeRate = 1.235235245
message = 'The price of this %s laptop is %d USD \n and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate) 
# %(brand, 1299, exchangeRate) - меткидля %.
# %s %d %4.2 - заполнители текста. %s %d заполняет текст. 
# %4.2f нужен для работы с числами с плавающей точкой. Где 4(количество основных чисел), а 2(Количество десятичных чисел).
print (message)

# Это не все функции %, их нужно изучать в документации Python