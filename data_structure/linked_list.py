

class Node:
    __slots__ = ['value', 'next_node', 'previous_node']

    def __init__(self, value):
        self.value = value

        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    """
    Структура данных двухсвязный список

    При size = 0 get и pop вернет None
    """
    def __init__(self):
        self.size = 0
        self._head = None
        self._tail = None

    def insert_head(self, value):
        cur_node = Node(value)

        if self._head is None:
            self._head = cur_node
            self._tail = cur_node

            self.size += 1
        else:
            previous_head = self._head

            previous_head.previous_node = cur_node
            cur_node.next_node = previous_head
            self._head = cur_node

            self.size += 1

    def insert_tail(self, value):
        cur_node = Node(value)

        if self._tail is None:
            self._head = cur_node
            self._tail = cur_node

            self.size += 1
        else:
            previous_tail = self._tail

            previous_tail.next_node = cur_node
            cur_node.previous_node = previous_tail
            self._tail = cur_node

            self.size += 1

    def pop_head(self):
        if self.size == 0:
            return None

        to_return = self._head.value
        current_head = self._head

        if self.size == 1:
            self._head = None
            self._tail = None

            self.size -= 1
        else:
            next_node = current_head.next_node
            next_node.previous_node = None

            self._head = next_node
            self.size -= 1

        del current_head

        return to_return

    def pop_tail(self):
        if self.size == 0:
            return None

        to_return = self._tail.value
        current_tail = self._tail

        if self.size == 1:
            self._head = None
            self._tail = None

            self.size -= 1
        else:
            previous_node = current_tail.previous_node
            previous_node.next_node = None

            self._tail = previous_node
            self.size -= 1

        del current_tail

        return to_return

    def get_head(self):
        if self.size == 0:
            return None
        else:
            return self._head.value

    def get_tail(self):
        if self.size == 0:
            return None
        else:
            return self._tail.value

    def remove(self, value):
        if self.size == 0:
            raise ValueError

        # итерация по всем узлам
        cur_node = self._head
        while cur_node is not None:
            if cur_node.value == value:
                # удаление узла
                # TODO удалять нужно меняя при этом _head и _tail
                previous_node = cur_node.previous_node
                next_node = cur_node.next_node
                if self.size == 1:
                    self._head = None
                    self._tail = None
                elif previous_node is not None:
                    previous_node.next_node = next_node
                elif next_node is not None:
                    next_node.previous_node = previous_node

                self.size -= 1
                break

            cur_node = cur_node.next_node

    def __iter__(self):
        self.__cur_node = self._head
        return self

    def __next__(self):
        cur_node = self.__cur_node

        if cur_node is None:
            raise StopIteration

        self.__cur_node = self.__cur_node.next_node

        return cur_node.value