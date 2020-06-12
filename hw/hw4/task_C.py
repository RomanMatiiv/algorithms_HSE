"""
Задача C
В данном списке из n ≤ 10^5 целых чисел найдите три числа,
произведение которых максимально.

Решение должно иметь сложность O(n), где n - размер списка.

Выведите три искомых числа в любом порядке.
"""
from algoritms.sorting.counting_sort import counting_sort

if __name__ == '__main__':
    array = [int(i) for i in input().strip().split()]

    sorted_arr = counting_sort(array)

    min_vals = sorted_arr[:3]
    max_vals = sorted_arr[-3:]

    if max_vals[0]*max_vals[1]*max_vals[2] > min_vals[0]*min_vals[1]*max_vals[2]:
        print(max_vals[0], max_vals[1], max_vals[2])
    else:
        print(min_vals[0], min_vals[1], max_vals[2])




