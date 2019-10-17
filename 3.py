
print('Введите координаты точки А:')
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))

print('Введите координаты точки B:')
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))

if x1 == x2:
    print ('Деление на ноль')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print('y = ',k,' * x  + ',b)
