from hw.hw1_2.task_G import pow_custom


def test_natural_number():
    assert pow_custom(1, 2) == pow(1, 2)
    assert pow_custom(2, 2) == pow(2, 2)
    assert pow_custom(1, 0) == pow(1, 0)
    assert pow_custom(1, 0) == pow(1, 0)
    assert pow_custom(0, 4) == pow(0, 4)
    assert pow_custom(0, 3) == pow(0, 3)
    assert pow_custom(0, 1) == pow(0, 1)
    assert pow_custom(0, 0) == pow(0, 0)
    assert pow_custom(12, 4) == pow(12, 4)


def test_rational_number():
    assert pow_custom(1/2, 2) == pow(1/2, 2)
    assert pow_custom(3/2, 2) == pow(3/2, 2)
    assert pow_custom(1/2, 0) == pow(1/2, 0)
    assert pow_custom(4/3, 0) == pow(4/3, 0)
    assert pow_custom(-2, 3) == pow(-2, 3)
    assert pow_custom(-2, 4) == pow(-2, 4)
