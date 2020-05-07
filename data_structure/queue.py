from data_structure.stack import Stack
from data_structure.stack import StackMin


class Queue:
    """
    Очередь реализованная на 2 стеках

    При size = 0 push и pop вернет None
    """
    def __init__(self):
        self._stack_inp = Stack()  # для того чтобы складывать элементы
        self._stack_out = Stack()  # для извлечения элементов
        self.size = 0

    def push(self, value):
        """Добавить в очередь value"""
        self._stack_inp.push(value)
        self.size += 1
        return None

    def pop(self):
        """Извлечь из очереди первый элемент"""
        if self.size == 0:
            result = None

        elif self._stack_out.size != 0:
            result = self._stack_out.pop()
            self.size -= 1

        else:
            self._move_all_elements_from_inp_to_out()
            result = self._stack_out.pop()
            self.size -= 1

        return result

    def front(self):
        """Вернуть первый элемент в очереди без извлечения"""
        if self.size == 0:
            result = None

        elif self._stack_out.size != 0:
            result = self._stack_out.back()

        else:
            self._move_all_elements_from_inp_to_out()
            result = self._stack_out.back()

        return result

    def _move_all_elements_from_inp_to_out(self):
        """Переместить все элементы из входного стека в выходной"""
        while self._stack_inp.size != 0:
            val = self._stack_inp.pop()
            self._stack_out.push(val)
        return None


class MinQueue:
    """
    Очередь реализованная на 2 стеках

    При size = 0 push,pop,min вернет None
    """
    def __init__(self):
        self._stack_inp = StackMin()  # для того чтобы складывать элементы
        self._stack_out = StackMin()  # для извлечения элементов
        self.size = 0

    def push(self, value):
        """Добавить в очередь value"""
        self._stack_inp.push(value)
        self.size += 1
        return None

    def pop(self):
        """Извлечь из очереди первый элемент"""
        if self.size == 0:
            result = None

        elif self._stack_out.size != 0:
            result = self._stack_out.pop()
            self.size -= 1

        else:
            self._move_all_elements_from_inp_to_out()
            result = self._stack_out.pop()
            self.size -= 1

        return result

    def front(self):
        """Вернуть первый элемент в очереди без извлечения"""
        if self.size == 0:
            result = None

        elif self._stack_out.size != 0:
            result = self._stack_out.back()

        else:
            self._move_all_elements_from_inp_to_out()
            result = self._stack_out.back()

        return result

    def min(self):
        """Вернуть минимум в очереди"""
        if self.size == 0:
            min_in_queue = None

        elif self._stack_out.size != 0:
            min_in_queue = self._get_min_from_two_stack()
        else:
            self._move_all_elements_from_inp_to_out()
            min_in_queue = self._get_min_from_two_stack()

        return min_in_queue

    def _move_all_elements_from_inp_to_out(self):
        """Переместить все элементы из входного стека в выходной"""
        while self._stack_inp.size != 0:
            val = self._stack_inp.pop()
            self._stack_out.push(val)
        return None

    def _get_min_from_two_stack(self):
        min_in_inp_stack = self._stack_inp.min()
        min_in_out_stack = self._stack_out.min()

        if (min_in_inp_stack is not None and
            min_in_out_stack is not None):
            min_in_queue = min(min_in_inp_stack, min_in_out_stack)
        elif min_in_out_stack is None:
            min_in_queue = min_in_inp_stack
        elif min_in_inp_stack is None:
            min_in_queue = min_in_out_stack

        return min_in_queue
