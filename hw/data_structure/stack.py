

class Stack:
    """
    Структура данных стек
    Реализованная через динамический массив

    При size = 0 back и pop вернет None
    """
    def __init__(self):
        self.size = 0
        self.array = []

    def push(self, value):
        """Добавить в стек value"""
        self.array.append(value)
        self.size += 1

        return None

    def pop(self):
        """Извлечь верхний элемент из стека"""
        if self.size == 0:
            last_value = None
        else:
            last_value = self.array[-1]
            self.size -= 1
            del self.array[-1]

        return last_value

    def back(self):
        """Возвращает последний элемент в стеке без извлечения"""
        if self.size == 0:
            return None
        else:
            return self.array[-1]


class StackMin:
    """Реализация стека с поддержкой минимума"""
    def __init__(self):
        self._stack = Stack()
        self._stack_min = Stack()
        self.size = 0

    def push(self, value):
        """Добавление элемента в стек"""
        self._stack.push(value)
        self.size += 1

        cur_min = self.min()

        if cur_min is None:
            self._stack_min.push(value)
        else:
            if value < cur_min:
                self._stack_min.push(value)
            else:
                self._stack_min.push(cur_min)

    def pop(self):
        """
        Извлечение элемента из стека

        Из пустого стека извлекается None
        """
        if self._stack.back() is not None:
            self.size -= 1
        self._stack_min.pop()
        return self._stack.pop()

    def back(self):
        """
        Возвращает последний элемент в стека без извлечения

        Из пустого стека возвращается None
        """
        return self._stack.back()

    def min(self):
        """Возвращает минимальный элемент в стеке"""
        return self._stack_min.back()