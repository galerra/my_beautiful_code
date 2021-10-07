from datetime import datetime
import time as tm
import sys

print('Cегодня я покажу вам, как написать букву "е" с помощью цифр')
tm.sleep(1)
print('Выделите деньги на мой стартап!')
tm.sleep(1)
a = input('Введите число:')
s = 2
for i in range(6):
    if s == 2:
        print('-',a,a,a)
    if s == 3 or s == 5:
        print('-',a,a,'-')
    if s == 4:   
        print(a,a,a,a)
    if s == 6:
        print(a,a,a,'-')
    s += 1
        
