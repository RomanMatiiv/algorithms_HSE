
def upper_bound(array, value) -> int:
    """
    Возвращает индекс первого элемента который > value

    Если такого нет, то индекс последнего элемента
    Args:
        array: отсортированный массив
        value: элемент на основе которого будем границу искать

    Returns: int(index)
    """
    if len(array) == 0:
        raise IndexError

    left = 0
    right = len(array) - 1

    while right > left:
        middle = (right + left)//2

        if array[middle] <= value:
            left = middle + 1
        else:
            right = middle

    return right


def lower_bound(array, value) -> int:
    """
    Возвращает индекс первого элемента который >= value

    Если такого нет, то индекс последнего элемента
    Args:
        array: отсортированный массив
        value: элемент на основе которого будем границу искать

    Returns: int(index)
    """
    if len(array) == 0:
        raise IndexError

    left = 0
    right = len(array) - 1

    while right > left:
        middle = (right + left)//2

        if array[middle] >= value:
            right = middle
        else:
            left = middle + 1
    return left


def binary_search(array, value) -> bool:
    """
    Проверяет вхождение элемента в массив

    Args:
        array: массив
        value: элемент вхождение которого хотим проверить

    Returns: bool
             True - элемент содержится в массиве
             False - элемент не содержится в массиве

    """
    left = 0
    right = len(array)

    while right > left:
        middle = (right + left)//2

        if array[middle] < value:
            left = middle + 1
        else:
            right = middle
    try:
        is_equal = array[left] == value
    except IndexError:
        is_equal = False

    return is_equal


def binary_search_2(array, value) -> bool:
    """
    Проверяет вхождение элемента в массив

    вариант 2 написанный на основе lower_bound и upper_bound
    Args:
        array: массив
        value: элемент вхождение которого хотим проверить

    Returns: bool
             True - элемент содержится в массиве
             False - элемент не содержится в массиве

    """
    lb_index = lower_bound(array, value)

    if array[lb_index] == value:
        return True
    else:
        return False