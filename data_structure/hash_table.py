from data_structure.linked_list import DoublyLinkedList


class Node:
    __slots__ = ['key', 'data']

    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashTable:
    """
    Реализация хеш таблицы
    Метод разрешения коллизий: метод цепочек
    """
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
        linked_list_index = self.hash_func(key) % self.size
        node = Node(key, val)

        # без коллизий
        if self.table[linked_list_index] is None:
            self.table[linked_list_index] = DoublyLinkedList()
            self.table[linked_list_index].insert_head(node)
        # коллизия
        else:
            self.table[linked_list_index].insert_tail(node)

        return None

    def remove(self, key) -> None:
        linked_list_index = self.hash_func(key) % self.size
        linked_list = self.table[linked_list_index]

        if linked_list is not None:
            for cur_node in linked_list:
                if cur_node.key == key:
                    linked_list.remove(cur_node)

    def has(self, key) -> bool:
        linked_list_index = self.hash_func(key) % self.size
        linked_list = self.table[linked_list_index]

        if linked_list is not None:
            for cur_node in linked_list:
                if cur_node.key == key:
                    return True
        return False

    def get(self, key):
        linked_list_index = self.hash_func(key) % self.size
        linked_list = self.table[linked_list_index]

        if linked_list is not None:
            for cur_node in linked_list:
                if cur_node.key == key:
                    return cur_node.data
        else:
            raise KeyError

    def __len__(self):
        raise NotImplemented
