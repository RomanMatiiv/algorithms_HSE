from data_structure.heap import MaxHeap
from data_structure.heap import MinHeap


def test_min_heap_push():
    heap_min = MinHeap()
    heap_min.push(1)
    heap_min.push(2)


def test_min_heap_min():
    heap_min = MinHeap()

    try:
        heap_min.min()
    except:
        pass
    else:
        raise AssertionError

    heap_min.push(1)
    assert heap_min.min() == 1

    heap_min.push(0)
    assert heap_min.min() == 0

    heap_min.push(3)
    assert heap_min.min() == 0


def test_min_heap_pop():
    heap_min = MinHeap()

    try:
        heap_min.pop_min()
    except:
        pass
    else:
        raise AssertionError

    heap_min.push(1)
    heap_min.push(3)
    assert heap_min.pop_min() == 1
    assert heap_min.min() == 3

    assert heap_min.pop_min() == 3

    try:
        heap_min.pop_min()
    except:
        pass
    else:
        raise AssertionError

    heap_min.push(5)
    heap_min.push(8)
    heap_min.push(9)

    assert heap_min.pop_min() == 5
    assert heap_min.pop_min() == 8
    assert heap_min.pop_min() == 9


def test_min_heap_heapify():
    heap = MinHeap([0, 1, 1, 2, 3])

    assert heap.min() == 0
    assert heap.pop_min() == 0
    assert heap.pop_min() == 1
    assert heap.pop_min() == 1
    assert heap.pop_min() == 2

    heap = MinHeap([1, 0, 2, 3, 1])

    assert heap.min() == 0
    assert heap.pop_min() == 0
    assert heap.pop_min() == 1
    assert heap.pop_min() == 1
    assert heap.pop_min() == 2


def test_max_heap_push():
    heap_max = MaxHeap()
    heap_max.push(1)
    heap_max.push(2)


def test_max_heap_max():
    heap_max = MaxHeap()

    try:
        heap_max.max()
    except:
        pass
    else:
        raise AssertionError

    heap_max.push(1)
    assert heap_max.max() == 1

    heap_max.push(2)
    assert heap_max.max() == 2

    heap_max.push(0)
    assert heap_max.max() == 2


def test_max_heap_pop():
    heap_max = MaxHeap()

    try:
        heap_max.pop_max()
    except:
        pass
    else:
        raise AssertionError

    heap_max.push(1)
    heap_max.push(3)
    assert heap_max.pop_max() == 3
    assert heap_max.max() == 1

    assert heap_max.pop_max() == 1

    try:
        heap_max.pop_max()
    except:
        pass
    else:
        raise AssertionError

    heap_max.push(9)
    heap_max.push(8)
    heap_max.push(5)

    assert heap_max.pop_max() == 9
    assert heap_max.pop_max() == 8
    assert heap_max.pop_max() == 5


def test_max_heap_heapify():
    heap = MaxHeap([5, 5, 4, 4, 3])

    assert heap.max() == 5
    assert heap.pop_max() == 5
    assert heap.pop_max() == 5
    assert heap.max() == 4
    assert heap.pop_max() == 4

    heap = MaxHeap([4, 3, 5, 4, 5])

    assert heap.max() == 5
    assert heap.pop_max() == 5
    assert heap.pop_max() == 5
    assert heap.max() == 4
    assert heap.pop_max() == 4
