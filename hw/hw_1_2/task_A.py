"""
Задача A. Установить значение бита в 1

Напишите программу, которая в заданном числе устанавливает
определенный бит в 1 (биты при этом нумеруются с нуля, начиная от младших).

"""
a, i = [int(i) for i in input().split()]

result = (1 << i) | a

print(result)

