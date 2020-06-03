from algoritms.sorting.heap_sort import heap_sort


def test_empty_array():
    arr = []
    res = []

    assert heap_sort(arr) == res


def test_one_element_array():
    arr = [3]
    res = [3]

    assert heap_sort(arr) == res


def test_sort_sorted_array():
    arr = [1, 2, 3, 4, 5]
    res = [1, 2, 3, 4, 5]

    assert heap_sort(arr) == res


def test_on_natural_number():
    arr = [3, 1, 5, 4, 8]
    res = sorted(arr)

    assert heap_sort(arr) == res


def test_on_rational_number():
    arr = [-1, 4, 0.5, -1.3, 4, 1, 7]
    res = sorted(arr)

    assert heap_sort(arr) == res


def test_on_negative_only_number():
    arr = [-1, -1.3, -4, -1, -7]
    res = sorted(arr)

    assert heap_sort(arr) == res