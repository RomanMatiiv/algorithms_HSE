from algoritms.sorting.merge_sort import merge_sort


class Node:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.a < other.a

    def __le__(self, other):
        return self.a <= other.a



def test_usual_case():
    arr_N = [3, 1, 4, 51, 1, 3, 4]
    arr_R = [3, 1.1, 4, 51.5, 1.1, 3.4, 4.9]

    result_N = merge_sort(arr_N)
    result_R = merge_sort(arr_R)

    true_result_N = sorted(arr_N)
    true_result_R = sorted(arr_R)

    assert result_N == true_result_N
    assert result_R == true_result_R


def test_save_order():
    arr = [Node(3, 2),
           Node(1, 2),
           Node(1, 1)]

    sorted_arr = merge_sort(arr)

    assert sorted_arr[0].a == 1
    assert sorted_arr[0].b == 2

    assert sorted_arr[1].a == 1
    assert sorted_arr[1].b == 1

    assert sorted_arr[2].a == 3
    assert sorted_arr[2].b == 2


def test_one_element():
    arr = [2]

    result = merge_sort(arr)
    true_result = sorted(arr)

    assert result == true_result


def test_empty_array():
    arr = []

    result = merge_sort(arr)
    true_result = sorted(arr)

    assert result == true_result
