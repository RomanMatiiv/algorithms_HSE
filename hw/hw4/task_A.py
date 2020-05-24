"""
Задача A
Даны два списка A и B упорядоченных по неубыванию.
Объедините их в один упорядоченный список С
(то есть он должен содержать len(A)+len(B) элементов).

Решение оформите в виде функции merge(A, B), возвращающей новый список.
Алгоритм должен иметь сложность O(len(A)+len(B)).
Модифицировать исходные списки запрещается.
Использовать функцию sorted и метод sort запрещается.
"""
from algoritms.sorting.merge_sort import merge

if __name__ == '__main__':
    arr_1 = [int(i) for i in input().strip().split()]
    arr_2 = [int(i) for i in input().strip().split()]

    merged_arrays = merge(arr_1, arr_2)

    for val in merged_arrays:
        print(val, end=" ")