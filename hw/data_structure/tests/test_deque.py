from hw.data_structure.deque import Deque


def test_push():
    deque = Deque()

    deque.push_front(1)
    assert deque.font() == 1
    assert deque.back() == 1

    deque.push_front(2)
    assert deque.back() == 1
    assert deque.font() == 2

    deque.push_back(1)
    deque.push_back(2)
    assert deque.font() == 2
    assert deque.back() == 2


def test_pop():
    deque = Deque()

    deque.push_back(1)
    assert deque.pop_front() == 1

    deque.push_front(1)
    assert deque.pop_back() == 1

    deque.push_front(1)
    deque.push_front(2)
    assert deque.pop_back() == 1
    assert deque.pop_back() == 2


def test_size():
    deque = Deque()

    assert deque.size == 0

    deque.push_front(1)
    assert deque.size == 1

    deque.pop_back()
    assert deque.size == 0

    deque.push_back(1)
    deque.push_front(2)
    assert deque.size == 2

    deque.pop_back()
    deque.pop_back()
    assert deque.size == 0