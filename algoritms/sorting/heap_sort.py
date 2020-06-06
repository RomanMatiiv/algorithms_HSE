from data_structure.heap import MinHeap


def heap_sort(array: list):
    sorted_array = []
    heap = MinHeap(array)

    while len(heap) > 0:
        cur_min_val = heap.pop_min()
        sorted_array.append(cur_min_val)

    return sorted_array

