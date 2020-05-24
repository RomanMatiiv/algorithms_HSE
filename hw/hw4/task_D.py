"""
Задача D

Дан список из N (N ≤ 2 * 105) элементов,которые принимают целые значения от 0 до 100.
Отсортируйте этот список в порядке неубывания элементов.
Выведите полученный список.
"""
from algoritms.sorting.counting_sort import counting_sort

if __name__ == '__main__':
    arr = [int(i) for i in input().strip().split()]

    sorted_arr = counting_sort(arr, min_val=0, max_val=100)

    for val in sorted_arr:
        print(val, end=" ")