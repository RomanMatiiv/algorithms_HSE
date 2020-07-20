from data_structure.linked_list import DoublyLinkedList


class Node:
    __slots__ = ['key', 'data']

    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __lt__(self, other):
        if self.data < other.data:
            return True
        elif self.data > other.data:
            return False
        elif self.data == other.data:
            if self.key < other.key:
                return False
            else:
                return True

    def __gt__(self, other):
        if self.data > other.data:
            return True
        elif self.data < other.data:
            return False
        elif self.data == other.data:
            if self.key > other.key:
                return False
            else:
                return True

class HashTable:
    """
    Реализация хеш таблицы
    Метод разрешения коллизий: метод цепочек
    """
    def __init__(self, capacity=8, hash_func=hash):
        self._capacity = capacity
        self._hash_func = hash_func  # TODO написать со своей хеш функцией
        self._size = 0
        self._load_factor = 0
        self._THRESHOLD_LOAD_FACTOR = 0.75

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
            self._load_factor = self._size/self._capacity

        # коллизия
        else:
            cur_node = self._get_node(key)

            if cur_node is None:
                self.table[linked_list_index].insert_tail(node)
                self._size += 1
                self._load_factor = self._size/self._capacity
            else:
                if cur_node.key == node.key:
                    cur_node.data = val

        if self._load_factor >= self._THRESHOLD_LOAD_FACTOR:
            self.__rehash()

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
                    self._load_factor = self._size/self._capacity
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
        self._capacity = self._capacity * 2

        old_table = self.table.copy()
        del self.table

        self.table = [None] * self._capacity
        self._size = 0
        self._load_factor = 0

        for ceil in old_table:
            if ceil is not None:
                for node in ceil:
                    self.insert(key=node.key,
                                val=node.data)

        del old_table

    def __len__(self):
        return self._size