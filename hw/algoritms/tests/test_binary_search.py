from hw.algoritms.binary_search import upper_bound
from hw.algoritms.binary_search import lower_bound
from hw.algoritms.binary_search import binary_search



def test_upper_bound():
    arr = [1, 2, 2, 2, 4, 6]

    assert upper_bound(arr, 2) == 4
    assert upper_bound(arr, 3) == 4
    assert upper_bound(arr, 1) == 1
    assert upper_bound(arr, 8) == 5
    assert upper_bound(arr, 0) == 0


def test_lower_bound():
    arr = [1, 2, 2, 2, 4, 6]

    assert lower_bound(arr, 2) == 1
    assert lower_bound(arr, 3) == 4
    assert lower_bound(arr, 1) == 0
    assert lower_bound(arr, 8) == 5
    assert lower_bound(arr, 0) == 0


def test_binary_search():
    arr = [1, 2, 2, 2, 4, 6]

    assert binary_search(arr, 2) is True
    assert binary_search(arr, 3) is False
    assert binary_search(arr, 1) is True
    assert binary_search(arr, 8) is False
    assert binary_search(arr, 0) is False
