from copy import copy


class MinHeap:
    def __init__(self, array=[]):
        self.heap = self._heapify(array)

    def push(self, value) -> None:
        """
        Вставляет элемент в кучу

        Args:
            value: Элемент который нужно вставить
        """
        self.heap.append(value)

        last_val_index = len(self.heap) - 1
        self._sift_up(self.heap, last_val_index)

        return None

    def pop_min(self):
        """
        Возвращает минимальный элемент в куче с извлечением

        Returns: минимальный элемент в куче
        """
        root = copy(self.heap[0])

        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._sift_down(self.heap, 0)

        return root

    def min(self):
        """
        Возвращает минимальный элемент

        (Корень дерева)
        """
        return self.heap[0]

    # TODO переписать за асимптотику O(n) а не O(nlogn)
    def _heapify(self, array: list) -> list:
        heap = []

        for val in array:
            heap.append(val)
            self._sift_up(heap, len(heap))

        return heap

    def _sift_up(self, array: list, index: int) -> None:
        """"""
        parent_index = (index - 1)//2

        while parent_index >= 0:
            if array[parent_index] > array[index]:
                # TODO вынести в swap
                cur_val = copy(array[index])
                parent_val = copy(array[parent_index])
                array[index] = parent_val
                array[parent_index] = cur_val

                index = parent_index
                parent_index = (index - 1)//2
            else:
                break

    def _sift_down(self, array: list, index: int) -> None:
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        while right_child_index < len(array):
            if (array[index] > array[left_child_index] or
                array[index] > array[right_child_index]):

                if array[right_child_index] < array[left_child_index]:
                    min_child_index = right_child_index
                else:
                    min_child_index = left_child_index

                # TODO вынести в swap
                cur_val = copy(array[index])
                child_val = copy(array[min_child_index])
                array[index] = child_val
                array[min_child_index] = cur_val

                index = min_child_index
                left_child_index = 2 * index + 1
                right_child_index = 2 * index + 2
            else:
                break


class MaxHeap:
    def __init__(self, array=[]):
        self.heap = self._heapify(array)

    def push(self, value) -> None:
        """
        Вставляет элемент в кучу

        Args:
            value: Элемент который нужно вставить
        """
        self.heap.append(value)

        last_val_index = len(self.heap) - 1
        self._sift_up(self.heap, last_val_index)

        return None

    def pop_max(self):
        """
        Возвращает максимальный элемент в куче с извлечением

        Returns: максимальный элемент в куче
        """
        root = copy(self.heap[0])

        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._sift_down(self.heap, 0)

        return root

    def max(self):
        """
        Возвращает максимальный элемент

        (Корень дерева)
        """
        return self.heap[0]

    # TODO переписать за асимптотику O(n) а не O(nlogn)
    def _heapify(self, array: list) -> list:
        heap = []

        for val in array:
            heap.append(val)
            self._sift_up(heap, len(heap))

        return heap

    def _sift_up(self, array: list, index: int) -> None:
        """"""
        parent_index = (index - 1)//2

        while parent_index >= 0:
            if array[parent_index] < array[index]:
                # TODO вынести в swap
                cur_val = copy(array[index])
                parent_val = copy(array[parent_index])
                array[index] = parent_val
                array[parent_index] = cur_val

                index = parent_index
                parent_index = (index - 1)//2
            else:
                break

    def _sift_down(self, array: list, index: int) -> None:
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        while right_child_index<len(array):
            if (array[index] < array[left_child_index] or
                array[index] < array[right_child_index]):

                if array[right_child_index] > array[left_child_index]:
                    max_child_index = right_child_index
                else:
                    max_child_index = left_child_index

                # TODO вынести в swap
                cur_val = copy(array[index])
                child_val = copy(array[max_child_index])
                array[index] = child_val
                array[max_child_index] = cur_val

                index = max_child_index
                left_child_index = 2 * index + 1
                right_child_index = 2 * index + 2
            else:
                break
