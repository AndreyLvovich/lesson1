# Вводятся три разных числа. Найти,
# какое из них является средним
# (больше одного, но меньше другого)

a = int(input('Введите число a  = '))
b = int(input('Введите число b  = '))
c = int(input('Введите число c  = '))

if c > a > b  or  b > a > c:
    print('Среднее число a = ',a)
elif a > b > c or  c > b > a:
    print('Среднее число b =  ',b)
else:
    print('Среднее число c =  ',c)