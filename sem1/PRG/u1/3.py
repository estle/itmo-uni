from math import sqrt

a, b, c = map(float, input('Введите стороны треугольника в одну строку через пробел: ').split())
if not(a + b > c and a + c > b and b + c > a): # Проверка на существование треугольника
    print('Ошибка. Такого тр-ка не существует!')
elif a==b==c:
    S = (a**2*sqrt(3))/4
    print('Площадь равностороннего треугольника = ', S)
else:
    p = (a+b+c)/2
    S = sqrt(p*(p-a)*(p-b)*(p-c))
    print('Площадь произвольного треугольника = ', S)


