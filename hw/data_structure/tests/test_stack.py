from hw.data_structure.stack import Stack


def test_push():
    stack = Stack()

    stack.push(1)
    assert stack.back() == 1
    assert stack.size == 1

    stack.push(3)
    assert stack.back() == 3


def test_pop():
    stack = Stack()

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
