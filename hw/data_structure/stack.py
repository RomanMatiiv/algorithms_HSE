from hw.data_structure.linked_list import LinkedList


class Stack:
    """
    Структура данных стек
    Реализованная через двух связный список
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
        back_value = self._stack.pop_head()
        self.size -= 1

        return back_value

    def back(self):
        """Вернуть верхний элемент стека не извлекая его """
        return self._stack.get_head()


class StackWithClear(Stack):
    """
    Стек, с поддержкой операции clear
    """
    def clear(self):
        """Удаляет все элементы из стека"""
        while self.size != 0:
            self.pop()
