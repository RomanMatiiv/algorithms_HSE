"""
Задача E

В обувном магазине продается обувь разного размера.
Известно, что одну пару обуви можно надеть на другую,
если она хотя бы на три размера больше.
В магазин пришел покупатель.
Требуется определить, какое наибольшее количество пар обуви
сможет предложить ему продавец так, чтобы он смог надеть их все одновременно.

Сначала вводится размер ноги покупателя
(обувь меньшего размера он надеть не сможет),
в следующей строке — размеры каждой пары обуви в магазине через пробел.
Размер — натуральное число, не превосходящее 100.
"""
from algoritms.sorting.counting_sort import counting_sort

if __name__ == '__main__':
    buyer_size = int(input())
    all_shoes = [int(i) for i in input().strip().split()]
    all_shoes = counting_sort(all_shoes)

    shoes_in_buyer = 0
    previous_shoes_size = -3
    for shoes_size in all_shoes:
        if (shoes_size >= buyer_size and
            shoes_size - previous_shoes_size >= 3):
            shoes_in_buyer += 1
            previous_shoes_size = shoes_size

    print(shoes_in_buyer)