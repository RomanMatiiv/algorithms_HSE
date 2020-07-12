from data_structure.linked_list import DoublyLinkedList


class Node:
    __slots__ = ['key', 'data']

    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __eq__(self, other):

        if (self.key == other.key and
            self.data == other.data):
            return True
        else:
            return False


class HashTable:
    """
    Реализация хеш таблицы
    Метод разрешения коллизий: метод цепочек
    """
    def __init__(self, capacity=8, hash_func=hash):
        self._capacity = capacity
        self._hash_func = hash_func  # TODO написать со своей хеш функцией
        self._size = 0
        self._alpha = None

        self.table = [None] * self._capacity

    def insert(self, key, val) -> None:
        """
        Вставка элемента

        Args:
            key: ключ для ассоциативного массива
            val: данные которые нужно вставить

        Returns: None
        """
        linked_list_index = self._hash_func(key) % self._capacity
        node = Node(key, val)

        # без коллизий
        if self.table[linked_list_index] is None:
            self.table[linked_list_index] = DoublyLinkedList()
            self.table[linked_list_index].insert_head(node)
            self._size += 1

        # коллизия
        else:
            cur_node = self._get_node(key)

            if cur_node is None:
                self.table[linked_list_index].insert_tail(node)
                self._size += 1
            else:
                if cur_node.key == node.key:
                    cur_node.data = val

        return None

    def remove(self, key) -> None:
        """
        удаление элемента из хеш таблицы

        Args:
            key: ключ элемента, который нужно удалить

        Returns: None
        """
        linked_list_index = self._hash_func(key) % self._capacity
        linked_list = self.table[linked_list_index]

        if linked_list is not None:
            for cur_node in linked_list:
                if cur_node.key == key:
                    linked_list.remove(cur_node)
                    self._size -= 1
        return None

    def has(self, key) -> bool:
        """
        Проверка содержится ли элемент в таблице

        Args:
            key: ключ элемента, содержание которого проверяем

        Returns: bool
                True - элемент содержится в таблице
                False - не содержится
        """
        linked_list_index = self._hash_func(key) % self._capacity
        linked_list = self.table[linked_list_index]

        if linked_list is not None:
            for cur_node in linked_list:
                if cur_node.key == key:
                    return True
        return False

    def get(self, key):
        """
        Возврат элемента по ключи

        Args:
            key: ключ элемента, который и нужно вернуть

        Returns: Элемент хеш таблицы с данным ключом
        """
        node = self._get_node(key)

        return node.data

    def _get_node(self, key):
        """
        Возврат узел(класс Node) по ключи

        Args:
            key: ключ элемента, который и нужно вернуть

        Returns: Node-у с данным ключом
        """
        linked_list_index = self._hash_func(key) % self._capacity
        linked_list = self.table[linked_list_index]

        if linked_list is not None:
            for cur_node in linked_list:
                if cur_node.key == key:
                    return cur_node
        else:
            raise KeyError

    def __rehash(self):
        raise NotImplemented

    def __len__(self):
        return self._size