from hw.data_structure.linked_list import DoublyLinkedList


def test_insert():
    llist = DoublyLinkedList()

    llist.insert_head(1)
    assert llist.get_head() == 1
    assert llist.get_tail() == 1

    llist.insert_tail(2)
    assert llist.get_tail() == 2

    llist.insert_head(3)
    assert llist.get_tail() == 2
    assert llist.get_head() == 3


def test_pop():
    llist = DoublyLinkedList()

    assert llist.get_head() is None
    assert llist.get_tail() is None

    llist.insert_head(1)
    assert llist.get_head() == 1
    assert llist.get_tail() == 1

    llist.insert_tail(2)
    assert llist.pop_head() == 1

    assert llist.get_head() == 2
    assert llist.get_tail() == 2

    llist.insert_head(3)
    assert llist.get_tail() == 2

    assert llist.get_head() == 3
    assert llist.pop_tail() == 2

    assert llist.get_head() == 3
    assert llist.get_tail() == 3


def test_size():
    llist = DoublyLinkedList()

    llist.insert_head(1)
    assert llist.size == 1

    llist.insert_tail(2)
    assert llist.size == 2

    llist.pop_head()
    assert llist.size == 1

    llist.pop_tail()
    assert llist.size == 0
