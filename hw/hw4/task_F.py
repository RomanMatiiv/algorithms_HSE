"""
Задача F
Даны два списка, упорядоченных по возрастанию
(каждый список состоит из различных элементов).
Найдите пересечение множеств элементов этих списков,
то есть те числа, которые являются элементами обоих списков.
Алгоритм должен иметь сложность O(len(A)+len(B)).
Решение оформите в виде функции Intersection(A, B).
Функция должна возвращать список пересечения данных списков в порядке возрастания элементов.
Модифицировать исходные списки запрещается.

Программа получает на вход два возрастающих списка, каждый в отдельной строке.

Программа должна вывести последовательность возрастающих чисел,являющихся элементами обоих списков.
"""


def intersection(a, b):
    all_value = a + b

    min_val = min(all_value)
    max_val = max(all_value)

    shift = min_val

    elements_between_max_min = max_val - min_val + 1
    counting_arr = [0] * elements_between_max_min

    for val in all_value:
        index = val - shift
        counting_arr[index] += 1

    intersection_array = []
    for i, count in enumerate(counting_arr):
        if count == 2:
            val = shift + i
            intersection_array.append(val)

    return intersection_array


if __name__ == '__main__':
    a = [int(i) for i in input().strip().split()]
    b = [int(i) for i in input().strip().split()]

    result = intersection(a, b)

    for val in result:
        print(val, end=" ")