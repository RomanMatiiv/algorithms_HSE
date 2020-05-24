"""
Задача G. Ручная сортировка

Вам необходимо реализовать алгоритм сортировки merge-sort.
"""
from algoritms.sorting.merge_sort import merge_sort

if __name__ == '__main__':
    _ = input()
    arr = [int(i) for i in input().strip().split()]

    sorted_arr = merge_sort(arr)

    for val in sorted_arr:
        print(val, end=" ")