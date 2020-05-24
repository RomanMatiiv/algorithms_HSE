from algoritms.sorting.counting_sort import counting_sort


def test_on_zero_to_100():
    arr = [3, 1, 2, 0, 4, 30, 44, 2, 1, 4]

    true_result = sorted(arr)
    result = counting_sort(arr)

    assert result == true_result


def test_with_minus_value():
    arr = [3, -2, 1, 34, 2, -8]
    true_result = sorted(arr)
    result = counting_sort(arr)
    assert result == true_result

    arr = [-3, -1, -2, -9]
    true_result = sorted(arr)
    result = counting_sort(arr)
    assert result == true_result


def test_on_one_element_arr():
    arr = [1]
    true_result = sorted(arr)
    result = counting_sort(arr)
    assert result == true_result
