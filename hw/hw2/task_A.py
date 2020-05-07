"""
Задача A. Стек с защитой от ошибок

Научитесь пользоваться стандартной структурой данных stack для целых чисел.
Напишите программу, содержащую описание стека и моделирующую работу стека,
реализовав все указанные здесь методы.
Программа считывает последовательность команд и в зависимости от команды
выполняет ту или иную операцию.
После выполнения каждой команды программа должна вывести одну строчку.
Возможные команды для программы:
    * push n
        Добавить в стек число n (значение n задается после команды).
        Программа должна вывести ok.
    * pop
        Удалить из стека последний элемент. Программа должна вывести его значение.
    * back
        Программа должна вывести значение последнего элемента, не удаляя его из стека.
    * size
        Программа должна вывести количество элементов в стеке.
    * clear
        Программа должна очистить стек и вывести ok.
    * exit
        Программа должна вывести bye и завершить работу.

Перед исполнением операций back и pop программа должна проверять,
содержится ли в стеке хотя бы один элемент.
Если во входных данных встречается операция back или pop, и при этом стек пуст,
то программа должна вместо числового значения вывести строку error.
"""
import sys
from data_structure.stack import Stack


class StackWithClear(Stack):
    """
    Стек, с поддержкой операции clear
    """
    def clear(self):
        """Удаляет все элементы из стека"""
        while self.size != 0:
            self.pop()


if __name__ == "__main__":
    stack = StackWithClear()

    for line in sys.stdin:
        line = line.strip()
        line = line.split(" ")

        command = line[0]

        if command == "push":
            value = line[1]
            stack.push(value)
            print("ok")

        elif command == "pop":
            val = stack.pop()
            if val:
                print(val)
            else:
                print("error")

        elif command == "back":
            val = stack.back()
            if val:
                print(val)
            else:
                print("error")

        elif command == "size":
            size = stack.size
            print(size)

        elif command == "clear":
            stack.clear()
            print("ok")

        elif command == "exit":
            print("bye")
            break