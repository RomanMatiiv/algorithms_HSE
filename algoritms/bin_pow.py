

def bin_pow(a, n):
    """
    Реализация алгоритма быстрого возведения в степень

    https://e-maxx.ru/algo/binary_pow
    """
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        reduced_power = bin_pow(a, n/2)
        return reduced_power * reduced_power
    elif n % 2 != 0:
        return a * bin_pow(a, n-1)