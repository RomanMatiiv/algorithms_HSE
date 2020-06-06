"""
Задача B

Отсортировать массив с помощью пирамидальной сортировки
"""
from algoritms.sorting.heap_sort import heap_sort


if __name__ == '__main__':
    _ = input()
    arr = [int(i) for i in input().strip().split()]

    sorted_arr = heap_sort(arr)

    for val in sorted_arr:
        print(val, end=" ")