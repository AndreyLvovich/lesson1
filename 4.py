# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает
# свои границы диапазона. Например, если надо получить
# случайный символ от 'a' до 'f',
# то вводятся эти символы.
# Программа должна вывести на экран
# любой символ алфавита от 'a' до 'f' включительно.
import random;

print('Введите целое число:')
n1 = int(input('начало диапазона'))
n2 = int(input('конец диапазона'))

print('Введите вещественное число:')
v1 = float(input('начало диапазона'))
v2 = float(input('конец диапазона'))

print('Введите символ:')
s1 = ord(input('начало диапазона'))
s2 = ord(input('конец диапазона'))

n = int( random.randint(n1 , n2) )
v = float( random.uniform(v1 , v2) )
s = random.randint(s1 , s2)

print('Случайное целое число: ', n)
print('Случайное вещественое число: ', v)
print('Случайный символ: ', chr(s))