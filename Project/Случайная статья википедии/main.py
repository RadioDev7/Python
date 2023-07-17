# By Артём Тарасов АС-21 ГПОУ КИТ
# Python project name - Случайнаая страница в википедии
# Python version - 3.10.5 64bit windows, запущенная через VScode
import requests # импорт модуля HTTP
from bs4 import BeautifulSoup # импорт модуля синтаксического анализа документов HTML
import webbrowser # импорт модуля для работы с браузером
import os  # импорт модуля
os.system("mode con cols=70 lines=20") # разрешение консоли

while True: # бесконечный цикл
    url = requests.get("https://ru.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    os.system('CLS')
    print("Открыть случайную страницу википедии? (Y/N)")
    ans = input("").lower()
    if ans == "y": # функция
        url = "https://ru.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans == "n":
        os.system('CLS')
        print("Пока!")
        continue
    else:
        os.system('CLS')
        print("Не принимается!")
        