from data_structure.linked_list import DoublyLinkedList

class Node:
    __slots__ = ['key', 'data']

    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashTable:
    def __init__(self, size=8, hash_func=hash):
        self.size = size
        self.alpha = None
        self.hash_func = hash_func  # TODO написать со своей хеш функцией

        self.table = [None] * self.size

    def insert(self, key, val) -> None:
        """
        Вставка элемента

        Args:
            key: ключ для ассоциативного массива
            val: данные которые нужно вставить

        Returns: None
        """
        # TODO отрефакторить а то слишком запутанно (cell node)
        cell_index = self.hash_func(key) % self.size

        node = Node(key, val)

        # без коллизий
        if self.table[cell_index] is None:
            self.table[cell_index] = DoublyLinkedList()
            self.table[cell_index].insert_head(node)
        # коллизия
        else:
            self.table[cell_index].insert_tail(node)

        return None

    def remove(self, key) -> None:
        # TODO добавить в DoublyLinkedList возможность удаления узла
        raise NotImplemented

    def has(self, key) -> bool:
        # TODO отрефакторить а то слишком запутанно (cell node)

        # TODO переписать добавив возможность итерирования по DoublyLinkedList
        cell_index = self.hash_func(key) % self.size
        cell = self.table[cell_index]

        if cell is not None:
            cur_node = cell._head

            while cur_node is not None:
                if cur_node.value.key == key:
                    return True
                else:
                    cur_node = cur_node.next_node

        return False

    def get(self, key):
        # TODO отрефакторить а то слишком запутанно (cell node)
        cell_index = self.hash_func(key) % self.size
        cell = self.table[cell_index]

        if cell is not None:
            cur_node = cell._head

            while cur_node is not None:
                if cur_node.value.key == key:
                    return cur_node.value.data
                else:
                    cur_node = cur_node.next_node

        else:
            raise KeyError


    def __len__(self):
        raise NotImplemented
