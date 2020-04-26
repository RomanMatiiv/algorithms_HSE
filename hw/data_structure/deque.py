from hw.data_structure.linked_list import LinkedList


class Deque:
    def __init__(self):
        self._deque = LinkedList()
        self.size = 0

    def push_front(self, value):
        raise NotImplemented

    def push_back(self, value):
        raise NotImplemented

    def pop_front(self):
        raise NotImplemented

    def pop_back(self):
        raise NotImplemented

    def font(self):
        raise NotImplemented

    def back(self):
        raise NotImplemented
