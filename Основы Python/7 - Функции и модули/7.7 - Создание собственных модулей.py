# 7.7 - Создание собственных модулей
'''
Допустим, нужно использовать функцию checkIf-Prime(), определенную ранее 
в другом сценарии Python. Вот как это делается: сначала сохраните код функции 
в файле с именем prime.py на рабочем столе. Файл prime.py должен содержать
следующий код:
    
def checkIfPrime (numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck%x == 0):
            return False
    return True

Затем создайте другой файл Python и присвойте ему имя 
usecheckifprime.py. Также сохраните его на рабочем столе. 
Файл usecheckifprime.py должен содержать следующий код:
'''
import prime
answer = prime.checkIfPrime(13)
print (answer)

'''
Но допустим, нужно хранить файлы prime.py и usecheck-if prime.py в разных каталогах. 
В этом случае необходимо добавить в usecheck-if prime.py код, который сообщает 
интерпретатору Python, где искать модуль.
Для хранения prime.py на диске C был создан каталог с именем MyPythonModules. 
В начало файла usecheckifprime.py необходимо добавить следующий код 
(перед строкой import prime):
'''
import sys
if 'C:\\MyPythonModules' not in sys.path:
    sys.path.append('C:\\MyPythonModules')
import test
answer1 = test.checkIfPrime(15)
print (answer1)
'''
sys.path представляет системный путь Python. Это список каталогов, 
которые Python просматривает в ходе поиска модулей и файлов. Приведенный выше код при-
соединяет каталог C:\MyPythonModules к системному пути вашего компьютера.
Теперь файл prime.py можно разместить в каталоге C:\MyPythonModules, 
а файл usecheckifprime.py — в любом другом каталоге на ваше усмотрение.
'''