
def merge_sort(array: list) -> list:
    if (len(array) == 1 or
        len(array) == 0):
        return array

    left, right = split(array)

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def split(arr: list):
    middle_ind = len(arr)//2

    left = arr[:middle_ind]
    right = arr[middle_ind:]

    return left, right


def merge(left: list,
          right: list) -> list:

    merged_list = []

    left_index = 0
    right_index = 0

    while True:
        # получаем элементы из массивов
        try:
            left_val = left[left_index]
            right_val = right[right_index]
        except IndexError:
            break

        # сравниваем их
        if left_val <= right_val:
            merged_list.append(left_val)
            left_index += 1
        else:
            merged_list.append(right_val)
            right_index += 1

    # записываем остаток
    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])

    return merged_list
