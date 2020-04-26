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

