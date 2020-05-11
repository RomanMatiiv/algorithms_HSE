"""
На прямой расположены стойла, в которые необходимо расставить коров так,
чтобы минимальное растояние между коровами было как можно больше.

В первой строке вводятся числа n (2 ≤ n ≤ 500000) – количество стойл
и k (1 < k < n) – количество коров.
Во второй строке задаются n натуральных чисел
в порядке возрастания – координаты стойл (координаты не превосходят 10^9)

Выведите одно число – наибольшее возможное допустимое расстояние между коровами
"""


def all_cows_in_stalls(min_distance, num_cows, stalls):
    num_cows -= 1
    previous_cows = stalls[0]

    for stall in stalls[1:]:
        if stall - previous_cows >= min_distance:
            num_cows -= 1
            previous_cows = stall

    if num_cows <= 0:
        return True
    else:
        return False


if __name__ == '__main__':
    n, k = map(int, input().strip().split())

    stalls = [int(i) for i in input().strip().split()]

    left_distance = 0
    right_distance = stalls[-1]

    while right_distance > left_distance:
        middle_distance = (left_distance + right_distance) // 2

        if all_cows_in_stalls(middle_distance, k, stalls):
            left_distance = middle_distance + 1
        else:
            right_distance = middle_distance

    print(right_distance - 1)



