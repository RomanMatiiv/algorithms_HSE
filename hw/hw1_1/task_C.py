"""
Задача C. Площадь треугольника

Даны длины сторон треугольника. Вычислите площадь треугольника.

Вводятся три положительных числа.
"""
from math import sqrt


def calc_triangle_area(a: float, b: float, c: float):
    """
    Считает площадь треугольника по длинам его сторон

    С помощью формулы Герона
    https://en.wikipedia.org/wiki/Heron%27s_formula

    Args:
        a: одна из сторон треугольника
        b: одна из сторон треугольника
        c: одна из сторон треугольника

    Returns: площадь треугольника
    """
    semi_perimeter = (a + b + c) / 2

    area = sqrt(semi_perimeter * (semi_perimeter - a) *
                                 (semi_perimeter - b) *
                                 (semi_perimeter - c))

    return area


a = float(input())
b = float(input())
c = float(input())

area = calc_triangle_area(a, b, c)
print(area)
