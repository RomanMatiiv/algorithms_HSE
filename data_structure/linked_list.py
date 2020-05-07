

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
    # TODO добавить удаление узлов (del Node)
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
