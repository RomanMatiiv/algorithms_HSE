from copy import copy


class MinHeap:
    def __init__(self, array=[]):
        self.heap = copy(array)  # TODO выяснить почему здесь баг
        self._heapify()

    def push(self, value) -> None:
        """
        Вставляет элемент в кучу

        Args:
            value: Элемент который нужно вставить
        """
        self.heap.append(value)

        last_val_index = len(self.heap) - 1
        self._sift_up(last_val_index)

        return None

    def pop_min(self):
        """
        Возвращает минимальный элемент в куче с извлечением

        Returns: минимальный элемент в куче
        """
        root = copy(self.heap[0])

        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._sift_down(0)

        return root

    def min(self):
        """
        Возвращает минимальный элемент

        (Корень дерева)
        """
        return self.heap[0]

    def _heapify(self) -> None:
        """
        Строит кучу из массива

        Переставляя элементы в массиве у которых есть дети
        """

        for index in range(len(self.heap)//2, -1, -1):
            self._sift_down(index)

    def _sift_up(self, index: int) -> None:
        """
        Просеивает элемент вверх

        Восстанавливая свойства кучи
        Args:
            index: индекс элемента который нужно просеить
        """
        parent_index = (index - 1)//2

        while parent_index >= 0:
            if self.heap[parent_index] > self.heap[index]:
                self._swap(index, parent_index)

                index = parent_index
                parent_index = (index - 1)//2
            else:
                break

    def _sift_down(self, index: int) -> None:
        """
        Просеивает элемент вниз

        Восстанавливая свойства кучи
        Args:
            index: индекс элемента который нужно просеить
        """
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        while right_child_index < len(self.heap):
            parent = self.heap[index]
            left_child = self.heap[left_child_index]
            right_child = self.heap[right_child_index]

            if (parent > left_child or
                parent > right_child):

                if right_child < left_child:
                    min_child_index = right_child_index
                else:
                    min_child_index = left_child_index

                self._swap(index, min_child_index)

                index = min_child_index
                left_child_index = 2 * index + 1
                right_child_index = 2 * index + 2
            else:
                break

        # обработка случая, когда свойство кучи будет нарушено
        # а правого дочернего узла не будет
        if left_child_index < len(self.heap):
            if self.heap[left_child_index] < self.heap[index]:
                self._swap(index, left_child_index)

    def _swap(self, index_1: int, index_2: int) -> None:
        """
        Меняет 2 элемента в куче местами

        Args:
            index_1: индекс 1 элемента
            index_2: индекс 2 элемента
        """
        val_1 = copy(self.heap[index_1])
        val_2 = copy(self.heap[index_2])

        self.heap[index_1] = val_2
        self.heap[index_2] = val_1

    def __len__(self):
        return len(self.heap)


class MaxHeap:
    def __init__(self, array=[]):
        self.heap = copy(array)  # TODO выяснить почему здесь баг
        self._heapify()

    def push(self, value) -> None:
        """
        Вставляет элемент в кучу

        Args:
            value: Элемент который нужно вставить
        """
        self.heap.append(value)

        last_val_index = len(self.heap) - 1
        self._sift_up(last_val_index)

        return None

    def pop_max(self):
        """
        Возвращает минимальный элемент в куче с извлечением

        Returns: минимальный элемент в куче
        """
        root = copy(self.heap[0])

        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._sift_down(0)

        return root

    def max(self):
        """
        Возвращает минимальный элемент

        (Корень дерева)
        """
        return self.heap[0]

    def _heapify(self) -> None:
        """
        Строит кучу из массива

        Переставляя элементы в массиве у которых есть дети
        """

        for index in range(len(self.heap)//2, -1, -1):
            self._sift_down(index)

    def _sift_up(self, index: int) -> None:
        """
        Просеивает элемент вверх

        Восстанавливая свойства кучи
        Args:
            index: индекс элемента который нужно просеить
        """
        parent_index = (index - 1)//2

        while parent_index >= 0:
            if self.heap[parent_index] < self.heap[index]:
                self._swap(index, parent_index)

                index = parent_index
                parent_index = (index - 1)//2
            else:
                break

    def _sift_down(self, index: int) -> None:
        """
        Просеивает элемент вниз

        Восстанавливая свойства кучи
        Args:
            index: индекс элемента который нужно просеить
        """
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        while right_child_index < len(self.heap):
            parent = self.heap[index]
            left_child = self.heap[left_child_index]
            right_child = self.heap[right_child_index]

            if (parent < left_child or
                    parent < right_child):

                if right_child > left_child:
                    min_child_index = right_child_index
                else:
                    min_child_index = left_child_index

                self._swap(index, min_child_index)

                index = min_child_index
                left_child_index = 2 * index + 1
                right_child_index = 2 * index + 2
            else:
                break

        # обработка случая, когда свойство кучи будет нарушено
        # а правого дочернего узла не будет
        if left_child_index < len(self.heap):
            if self.heap[left_child_index] > self.heap[index]:
                self._swap(index, left_child_index)

    def _swap(self, index_1: int, index_2: int) -> None:
        """
        Меняет 2 элемента в куче местами

        Args:
            index_1: индекс 1 элемента
            index_2: индекс 2 элемента
        """
        val_1 = copy(self.heap[index_1])
        val_2 = copy(self.heap[index_2])

        self.heap[index_1] = val_2
        self.heap[index_2] = val_1

    def __len__(self):
        return len(self.heap)
