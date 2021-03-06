"""
Задача C. Очередь с защитой от ошибок

Научитесь пользоваться стандартной структурой данных queue для целых чисел.
Напишите программу, содержащую описание очереди и моделирующую работу очереди,
реализовав все указанные здесь методы.
Программа считывает последовательность команд и в зависимости от команды
выполняет ту или иную операцию.
После выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:
    push n - Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.
    pop - Удалить из очереди первый элемент. Программа должна вывести его значение.
    front - Программа должна вывести значение первого элемента, не удаляя его из очереди.
    size - Программа должна вывести количество элементов в очереди.
    clear - Программа должна очистить очередь и вывести ok.
    exit - Программа должна вывести bye и завершить работу.

Перед исполнением операций front и pop программа должна проверять,
содержится ли в очереди хотя бы один элемент.
Если во входных данных встречается операция front или pop,
и при этом очередь пуста, то программа должна вместо числового значения
вывести строку error.
"""
import sys
from data_structure.queue import Queue


class QueueWithClear(Queue):
    def clear(self):
        while self.size != 0:
            self.pop()


if __name__ == "__main__":
    queue = QueueWithClear()

    for line in sys.stdin:
        line = line.strip()
        line = line.split(" ")

        command = line[0]

        if command == "push":
            value = line[1]
            queue.push(value)
            print("ok")

        elif command == "pop":
            val = queue.pop()
            if val:
                print(val)
            else:
                print("error")

        elif command == "front":
            val = queue.front()
            if val:
                print(val)
            else:
                print("error")

        elif command == "size":
            size = queue.size
            print(size)

        elif command == "clear":
            queue.clear()
            print("ok")

        elif command == "exit":
            print("bye")
            break