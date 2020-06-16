"""
Задача H

Во время лыжных соревнований N спортсменов стартуют с интервалом в 1 минуту.
Скорость каждого лыжника на дистанции постоянна:
i-й лыжник преодолевает 1 км за wi минут.
Длина трассы равна L км.
Считается, что i-й лыжник обогнал j-го (совершил обгон),
если он стартовал позже j-го, а пришёл к финишу раньше него.

Подсчитайте суммарное число совершённых во время гонки обгонов.

Первая строка входного файла содержит два целых числа N и L.
Во второй строке через пробел расположены N целых чисел w_i.
"""

# if __name__ == '__main__':
#     n, l = [int(i) for i in input().strip().split()]
#
#     finish_times = [int(i)*l for i in input().strip().split()]
#     finish_times = finish_times[::-1]
#
#     overtake = 0
#     for i, time_i in enumerate(finish_times):
#         start_lag = 1
#         for time_j in finish_times[i+1:]:
#                 if time_i + start_lag < time_j:
#                     overtake += 1
#                 start_lag += 1
#
#     print(overtake)


def merge_sort(array: list, ) -> list:
    if (len(array) == 1 or
        len(array) == 0):
        return array

    left, right = split(array)

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def split(arr: list):
    middle_ind = len(arr)//2

    left = arr[:middle_ind]
    right = arr[middle_ind:]

    return left, right


def merge(left: list,
          right: list) -> list:

    merged_list = []

    left_index = 0
    right_index = 0

    global OVERTAKE

    while True:
        # получаем элементы из массивов
        try:
            left_val = left[left_index]
            right_val = right[right_index]
        except IndexError:
            break

        # сравниваем их
        if left_val <= right_val:
            merged_list.append(left_val)
            left_index += 1
        else:
            merged_list.append(right_val)
            right_index += 1
            OVERTAKE += len(left) - left_index

    # записываем остаток
    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])

    return merged_list


if __name__ == '__main__':
    _, l = [int(i) for i in input().strip().split()]

    duration = [int(i)*l for i in input().strip().split()]
    finish_times = [val+i for i, val in enumerate(duration)]

    OVERTAKE = 0

    merge_sort(finish_times)

    print(OVERTAKE)

