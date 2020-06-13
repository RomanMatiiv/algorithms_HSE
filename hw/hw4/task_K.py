"""
Задача K

Медиана последовательности — это элемент, который стоит в середине
отсортированной последовательности. Например 5, в последовательности 1 5 7

В случае массива четной длины в рамках этой задачи
будем всегда брать элемент с меньшим индексом.

Для заданной последовательности выведите медианы каждого его префикса.
Гарантируется, что элементы последовательности не повторяются.
"""
from data_structure.heap import MinHeap
from data_structure.heap import MaxHeap


class PrefixWithMedian:
    def __init__(self):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()

    def insert(self, val) -> None:
        len_prefix = len(self.max_heap) + len(self.min_heap)

        if len_prefix <= 1:
            self.min_heap.push(val)
        else:
            ref_val = self.min_heap.min()

            if len_prefix % 2 == 0:
                self._insert_and_shift_median(val, ref_val)
            else:
                self._insert_and_keep_median(val, ref_val)

    def get_median(self):
        return self.min_heap.min()

    def get_prefix(self):
        raise NotImplemented

    def _insert_and_shift_median(self, new_val, cur_median) -> None:
        """
        Вставка элемента если индекс медианного элемента изменится

        Те
        len(prefix) % 2 = 0
        """
        if new_val < cur_median:
            self.max_heap.push(new_val)
        else:
            self.min_heap.pop_min()
            self.max_heap.push(cur_median)
            self.min_heap.push(new_val)

    def _insert_and_keep_median(self, new_val, cur_median) -> None:
        """
        Вставка элемента если индекс медианного элемента не изменится

        Те
        len(prefix) % 2 = 1
        """
        if new_val > cur_median:
            self.min_heap.push(new_val)
        else:
            if self.max_heap.max() < new_val:
                self.min_heap.push(new_val)
            else:
                last_max_heap = self.max_heap.pop_max()
                self.max_heap.push(new_val)
                self.min_heap.push(last_max_heap)


if __name__ == '__main__':
    prefix_with_median = PrefixWithMedian()

    _ = input()
    arr = [int(i) for i in input().strip().split()]

    for val in arr:
        prefix_with_median.insert(val)
        print(prefix_with_median.get_median(), end=" ")

