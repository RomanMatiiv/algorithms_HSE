"""
Задача F. Приближенный двоичный поиск

Используйте lower_bound и, возможно, -- для итераторов,
для реализации приближенного двоичного поиска.

В первой строке входных данных содержатся числа N и K.
Во второй строке задаются N чисел первого массива, отсортированного по неубыванию,
а в третьей строке – K чисел второго массива.
Каждое число в обоих массивах по модулю не превосходит 2⋅10**9.

Для каждого из K чисел выведите в отдельную строку число из первого массива,
наиболее близкое к данному. Если таких несколько, выведите меньшее из них.
"""
from hw.algoritms.binary_search import lower_bound
from hw.algoritms.binary_search import upper_bound

if __name__ == "__main__":
    _ = input()
    array = [int(i) for i in input().strip().split()]
    requests = [int(i) for i in input().strip().split()]

    for request in requests:
        lb_index = lower_bound(array, request)
        ub_index = upper_bound(array, request)

        # элемент >= рассматриваемому
        next_el = array[ub_index]

        # элемент <= рассматриваемому
        if lb_index != 0 and array[lb_index] > request:
            previous_el = array[lb_index - 1]
        else:
            previous_el = array[lb_index]

        # выбор ближайшего
        if abs(next_el - request) < abs(previous_el - request):
            print(next_el)
        else:
            print(previous_el)