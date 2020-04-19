"""
Задача D. Сумма факториалов

По данному натуральном n вычислите сумму факториалов.
В решении этой задачи можно использовать только один цикл.

Вводится натуральное число n.
"""
n = int(input())

previous_factorial = 1
sum_factorials = 0

for i in range(1, n+1):
    current_factorial = previous_factorial * i
    sum_factorials += current_factorial

    previous_factorial = current_factorial

print(sum_factorials)
