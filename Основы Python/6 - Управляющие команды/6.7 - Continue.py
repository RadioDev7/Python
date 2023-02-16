# 6.7 - Continue
# При выполнении команды continue оставшаяся часть цикла после continue 
# пропускается для текущей итерации
j = 0
for i in range(5):
    j = j + 2
    print ('\ni = ', i, ', j = ', j)
    print("Прибавить число на 2")
    if j == 6:
        print ('НУЖНОЕ ЧИСЛО j=6')
        continue