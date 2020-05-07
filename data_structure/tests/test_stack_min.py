from data_structure.stack import StackMin


def test_push():
    stack = StackMin()

    stack.push(1)
    assert stack.back() == 1
    assert stack.size == 1

    stack.push(3)
    assert stack.back() == 3


def test_pop():
    stack = StackMin()

    stack.push(1)
    assert stack.size == 1
    assert stack.pop() == 1
    assert stack.size == 0

    stack.push(3)
    stack.push(1)
    assert stack.pop() == 1
    assert stack.size == 1
    assert stack.pop() == 3
    assert stack.size == 0


def test_min():
    stack = StackMin()

    stack.push(4)
    assert stack.min() == 4

    stack.push(1)
    assert stack.min() == 1

    stack.push(3)
    assert stack.min() == 1

    stack.pop()
    stack.pop()
    assert stack.min() == 4