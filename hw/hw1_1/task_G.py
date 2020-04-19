"""
Задача G. Квадратное уравнение - 2

Даны произвольные действительные коэффициенты a, b, c.
Решите уравнение ax2+bx+c=0.

Вводятся три действительных числа.

Решение https://www.cyberforum.ru/python-beginners/thread2520182.html
"""

from math import sqrt


def discriminant(a: float, b: float, c: float):
    D = b**2 - 4*a*c
    return D


a = float(input())
b = float(input())
c = float(input())

D = discriminant(a, b, c)

# квадратное уравнение
if a != 0:
    if D > 0:
        x_1 = (-b + sqrt(D))/2*a
        x_2 = (-b - sqrt(D))/2*a

        if x_1 <= x_2:
            print(2,x_1,x_2)
        else:
            print(2,x_2,x_1)

    elif D == 0:
        x = -b/2*a
        print(1,x)

    elif D < 0:
        print(0)
# линейное уравнение
elif b != 0:
    x = -(c/b)
    print(1,x)
# нет решения
elif c != 0:
    print(0)
# бесконечно много решений
elif a==b==c==0:
    print(3)