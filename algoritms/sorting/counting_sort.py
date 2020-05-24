

def counting_sort(array: list,
                  min_val=None,
                  max_val=None) -> list:
    """
    Сортировка подсчетом

    Только для множеств, которые принадлежат Z

    Args:
        array: массив который нужно отсортировать
        min_val: минимальный элемент в массиве
        max_val: максимальный элемент в массиве

    Returns: отсортированный массив

    """
    if min_val is None:
        min_val = min(array)
    if max_val is None:
        max_val = max(array)

    # для возможности работы с отрицательными числами
    shift = min_val

    elements_between_max_min = max_val - min_val + 1
    counting_arr = [0] * elements_between_max_min

    for val in array:
        index = val - shift
        counting_arr[index] += 1

    sorted_array = []
    for i, count in enumerate(counting_arr):
        while count != 0:
            val = shift + i
            sorted_array.append(val)
            count -= 1

    return sorted_array
