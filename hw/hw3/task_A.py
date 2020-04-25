def binary_search(arr, val):
    """Реализация бинарного поиска

        где arr: это отсортированный массив
    """
    finished = False

    while not finished:
        l = len(arr)//2
        r = len(arr)//2 + 1

        if arr[l] < val:
            arr = arr[:l]
        elif arr[r] >= val:
            arr = arr[r+1:]

    return arr[l]


binary_search([1, 2, 3, 4, 5], 3)

# if __name__ == "__main__":
#     _ = input()
#
#     arr = [int(i) for i in input().spli(" ")]
#     requests = [int(i) for i in input().spli(" ")]

