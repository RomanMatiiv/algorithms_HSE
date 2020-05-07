"""
Задача C. Массивы (python)

Даны два массива.
Для каждого элемента второго массива определите,
сколько раз он встречается в первом массиве.
Используйте lower_bound и upper_bound, а также вычитание итераторов.

Первая строка входных данных содержит одно число
N  – количество элементов в первом массиве.
Далее идет N целых чисел– элементы первого массива,

Далее идет количество элементов M во втором массиве
и M элементов второго массива.
"""
from algoritms.binary_search import lower_bound
from algoritms.binary_search import upper_bound

if __name__ == "__main__":
    # N
    _ = input()
    array = [int(i) for i in input().strip().split()]
    array.sort()

    # M
    _ = input()
    requests = [int(i) for i in input().strip().split()]

    for request in requests:
        lb_index = lower_bound(array, request)
        ub_index = upper_bound(array, request)

        # если есть элемент > request
        if (array[lb_index] == request and
            array[ub_index] != request):
            number = ub_index - lb_index
            print(number)
        # если request - это максимум
        elif (array[lb_index] == request and
              array[ub_index] == request):
            number = ub_index - lb_index + 1
            print(number)
        # request нет в массиве
        else:
            print(0)
