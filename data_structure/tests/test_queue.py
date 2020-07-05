from data_structure.queue_custom import Queue


def test_push():
    queue = Queue()

    queue.push(1)
    assert queue.front() == 1
    assert queue.size == 1

    queue.push(2)
    assert queue.front() == 1
    assert queue.size == 2


def test_pop():
    queue = Queue()

    queue.push(1)
    assert queue.pop() == 1
    assert queue.size == 0

    queue.push(2)
    assert queue.front() == 2
    assert queue.size == 1

    queue.push(3)
    queue.push(4)
    assert queue.pop() == 2
    assert queue.size == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.size == 0


def test_front():
    queue = Queue()

    queue.push(1)
    assert queue.front() == 1
    assert queue.size == 1

    queue.push(2)
    queue.push(3)
    assert queue.front() == 1
    assert queue.size == 3

    for i in range(4, 100):
        queue.push(i)
    assert queue.front() == 1


def test_on_case_from_hw2_task():
    queue = Queue()

    queue.push(2)
    queue.push(4)
    queue.push(6)
    queue.push(8)
    queue.push(0)

    assert queue.pop() == 2
