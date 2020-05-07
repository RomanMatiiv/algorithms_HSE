

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
        return bin_pow(a*a, n/2)
    elif n % 2 != 0:
        return a * bin_pow(a, n-1)