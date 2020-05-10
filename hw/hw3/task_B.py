"""
Задача B. Очень Лёгкая Задача

Сегодня утром жюри решило добавить в вариант олимпиады еще одну задачу.
Ответственный секретарь Оргкомитета напечатал её условие в одном экземпляре,
и теперь ему нужно до начала олимпиады успеть сделать ещё n копий.

В его распоряжении имеются два ксерокса,
один из которых копирует лист за х секунд, а другой — за y.
Разрешается использовать как один ксерокс, так и оба одновременно.
Можно копировать не только с оригинала, но и с копии.

Помогите ему выяснить, какое минимальное время для этого потребуется.

На вход программы поступают три натуральных числа n, x и y, разделенные пробелом

Выведите одно число — минимальное время в секундах, необходимое для получения n копий.
"""


def is_deadline_keeping(deadline, copy_need, speed_1, speed_2):
    make_copy = deadline//speed_1 + deadline//speed_2

    if make_copy >= copy_need:
        return True
    else:
        return False


if __name__ == "__main__":
    number_copy, printer_1_speed, printer_2_speed = [int(i) for i in input().strip().split()]

    # делаем 1 копию на самом быстром
    if printer_1_speed < printer_2_speed:
        first_copy_duration = printer_1_speed
    else:
        first_copy_duration = printer_2_speed
    number_copy -= 1

    # узнаем сколько нужно минимум времени на оставшиеся
    left_deadline = 0
    right_deadline = number_copy * printer_1_speed

    while right_deadline > left_deadline:
        middle_deadline = (left_deadline + right_deadline) // 2

        if is_deadline_keeping(middle_deadline,
                               number_copy,
                               printer_1_speed,
                               printer_2_speed):
            right_deadline = middle_deadline
        else:
            left_deadline = middle_deadline + 1

    print(left_deadline + first_copy_duration)
