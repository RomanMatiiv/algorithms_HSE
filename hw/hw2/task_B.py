"""
Задача B. Правильная скобочная последовательность

Программа получает на вход последовательность из скобок
(открывающихся и закрывающихся скобок трех видов).
Длина последовательности не превышает 255 символов.
Последовательность не содержит пробелов
(но после последнего символа могут идти пробелы и переходы на новую строку).
"""
from hw.data_structure.stack import Stack

OPENING_BRACKETS = ["(", "[", "{"]

BRACKETS_MAPPING = {")": "(",
                    "]": "[",
                    "}": "{"}

inp = input().strip()
stack = Stack()
result = None

for bracket in inp:
    if bracket in OPENING_BRACKETS:
        stack.push(bracket)
    else:
        if BRACKETS_MAPPING[bracket] != stack.pop():
            result = "no"
            break

if stack.size == 0 and not result:
    result = "yes"
else:
    result = "no"

print(result)
