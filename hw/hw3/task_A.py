"""
Задача A. Двоичный поиск

В первой строке входных данных содержатся натуральные числа N и K .
Во второй строке задаются N элементов первого массива,
а в третьей строке – K элементов второго массива.
Элементы обоих массивов - целые числа,
каждое из которых по модулю не превосходит 10**9

Требуется для каждого из K чисел вывести в отдельную строку
"YES", если это число встречается в первом массиве
"NO" в противном случае.
"""

from hw.algoritms.binary_search import binary_search


if __name__ == "__main__":
    _ = input()

    arr = [int(i) for i in input().strip().split(" ")]
    requests = [int(i) for i in input().strip().split(" ")]

    for request in requests:
        if binary_search(arr, request):
            print("YES")
        else:
            print("NO")

