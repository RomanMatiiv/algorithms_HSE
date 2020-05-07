"""
Задача E Дек с защитой от ошибок

Научитесь пользоваться стандартной структурой данных deque для целых чисел.
Напишите программу, содержащую описание дека и моделирующую работу дека,
реализовав все указанные здесь методы.

Программа считывает последовательность команд и в зависимости
от команды выполняет ту или иную операцию.
После выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:
    * push_front n: Добавить (положить) в начало дека новый элемент.
                    Программа должна вывести ok.

    * push_back n: Добавить (положить) в конец дека новый элемент.
                   Программа должна вывести ok.

    * pop_front: Извлечь из дека первый элемент.
                 Программа должна вывести его значение.

    * pop_back: Извлечь из дека последний элемент.
                Программа должна вывести его значение.

    * front: Узнать значение первого элемента (не удаляя его).
             Программа должна вывести его значение.

    * back: Узнать значение последнего элемента (не удаляя его).
            Программа должна вывести его значение.

    * size: Вывести количество элементов в деке.

    * clear: Очистить дек (удалить из него все элементы) и вывести ok.

    * exit: Программа должна вывести bye и завершить работу.

Гарантируется, что количество элементов в деке в любой момент не превосходит 100.
Перед исполнением операций pop_front, pop_back, front, back
программа должна проверять, содержится ли в деке хотя бы один элемент.
Если во входных данных встречается операция pop_front, pop_back, front, back,
и при этом дек пуст, то программа должна вместо числового значения
вывести строку error.
"""

import sys
from data_structure.deque import Deque


class DequeWithClear(Deque):
    def clear(self):
        while self.size != 0:
            self.pop_front()


if __name__ == "__main__":
    deque = DequeWithClear()

    for line in sys.stdin:
        line = line.strip()
        line = line.split(" ")

        command = line[0]

        if command == "push_front":
            value = line[1]
            deque.push_front(value)
            print("ok")

        elif command == "push_back":
            value = line[1]
            deque.push_back(value)
            print("ok")

        elif command == "pop_front":
            val = deque.pop_front()
            if val:
                print(val)
            else:
                print("error")

        elif command == "pop_back":
            val = deque.pop_back()
            if val:
                print(val)
            else:
                print("error")

        elif command == "front":
            val = deque.front()
            if val:
                print(val)
            else:
                print("error")

        elif command == "back":
            val = deque.back()
            if val:
                print(val)
            else:
                print("error")

        elif command == "size":
            size = deque.size
            print(size)

        elif command == "clear":
            deque.clear()
            print("ok")

        elif command == "exit":
            print("bye")
            break