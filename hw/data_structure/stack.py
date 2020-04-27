from hw.data_structure.linked_list import LinkedList


class Stack:
    """
    Структура данных стек
    Реализованная через двух связный список

    При size = 0 push и pop вернет None
    """
    def __init__(self):
        self._stack = LinkedList()
        self.size = 0

    def push(self, value):
        """Добавить в стек число value"""
        self._stack.insert_head(value)
        self.size += 1

    def pop(self):
        """Извлечь верхний элемент из стека"""
        first_val = self._stack.pop_head()

        if first_val is not None:
            self.size -= 1

        return first_val

    def back(self):
        """Вернуть верхний элемент стека не извлекая его """
        return self._stack.get_head()


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