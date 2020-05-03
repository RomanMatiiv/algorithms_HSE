from hw.algoritms.bin_pow import bin_pow


def test_natural_number():
    assert bin_pow(1, 2) == pow(1, 2)
    assert bin_pow(2, 2) == pow(2, 2)
    assert bin_pow(1, 0) == pow(1, 0)
    assert bin_pow(1, 0) == pow(1, 0)
    assert bin_pow(0, 4) == pow(0, 4)
    assert bin_pow(0, 3) == pow(0, 3)
    assert bin_pow(0, 1) == pow(0, 1)
    assert bin_pow(0, 0) == pow(0, 0)
    assert bin_pow(12, 4) == pow(12, 4)


def test_rational_number():
    assert bin_pow(1/2, 2) == pow(1/2, 2)
    assert bin_pow(3/2, 2) == pow(3/2, 2)
    assert bin_pow(1/2, 0) == pow(1/2, 0)
    assert bin_pow(4/3, 0) == pow(4/3, 0)
    assert bin_pow(-2, 3) == pow(-2, 3)
    assert bin_pow(-2, 4) == pow(-2, 4)
