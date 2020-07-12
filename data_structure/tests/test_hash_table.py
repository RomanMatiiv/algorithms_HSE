from data_structure.hash_table import HashTable


def test_insert():
    ht = HashTable()

    ht.insert(1, None)
    ht.insert("f", None)
    ht.insert(9, None)


def test_has():
    ht = HashTable()

    ht.insert(1, None)
    ht.insert("f", None)
    ht.insert(9, None)

    assert ht.has(1) is True
    assert ht.has("f") is True
    assert ht.has(4) is False
    assert ht.has(9) is True


def test_remove():
    ht = HashTable()

    ht.insert(1, None)
    assert ht.has(1) is True

    ht.remove(1)
    assert ht.has(1) is False

    try:
        ht.remove(4)
    except KeyError:
        pass


def test_get():
    ht = HashTable()

    ht.insert(1, [1, 2, 3])
    assert ht.get(1) == [1, 2, 3]

    try:
        ht.get(4)
    except KeyError:
        pass

    ht.insert(9, "r")
    assert ht.get(9) == "r"


def test_size():
    ht = HashTable()

    assert len(ht) == 0

    ht.insert(key=1, val=None)
    assert len(ht) == 1
    ht.insert(key=2, val=None)
    assert len(ht) == 2
    ht.insert(key=1, val=None)
    assert len(ht) == 2

    ht.insert(key=3, val=None)
    assert len(ht) == 3
    ht.insert(key=5, val=None)
    assert len(ht) == 4
    ht.insert(key=5, val=None)
    assert len(ht) == 4

    ht.remove(1)
    assert len(ht) == 3


def test_the_same_key():
    ht = HashTable()

    ht.insert(1, "a")
    ht.insert(9, "b")

    assert ht.has(1) is True
    assert ht.get(1) == "a"
    assert ht.has(9) is True
    assert ht.get(9) == "b"
    assert len(ht) == 2

    ht.insert(1, "k")

    assert ht.has(1) is True
    assert ht.get(1) == "k"
    assert ht.has(9) is True
    assert ht.get(9) == "b"
    assert len(ht) == 2

