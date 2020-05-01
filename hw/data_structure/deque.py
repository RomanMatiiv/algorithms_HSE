from hw.data_structure.linked_list import DoublyLinkedList


class Deque:
    """
    Структура данных дек реализованная на 2-ух связном списке

    При size = 0 push и pop вернет None
    """
    def __init__(self):
        self._deque = DoublyLinkedList()
        self.size = 0

    def push_front(self, value):
        self._deque.insert_head(value)
        self.size += 1

    def push_back(self, value):
        self._deque.insert_tail(value)
        self.size += 1

    def pop_front(self):
        if self.size > 0:
            self.size -= 1

        return self._deque.pop_head()

    def pop_back(self):
        if self.size > 0:
            self.size -= 1

        return self._deque.pop_tail()

    def front(self):
        return self._deque.get_head()

    def back(self):
        return self._deque.get_tail()
