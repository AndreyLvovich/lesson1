#Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

alfavit = list('abcdefghijklmnopqrstuvwxyz')

bukva1 = input('Введите первую букву')
bukva2 = input('Введите вторую букву')

number1 = alfavit.index(bukva1) + 1
number2 = alfavit.index(bukva2) + 1
r = abs(number2 - number1)

print('Буква ',bukva1,' находиться на ',number1,' месте')
print('Буква ',bukva2,' находиться на ',number2,' месте')
print('Количество букв между буквой ',bukva1,' и буквой ',bukva2,' = ',r)
