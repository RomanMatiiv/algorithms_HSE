from typing import NoReturn


class HashTable:
    def __init__(self):
        self.size = None
        self.alpha = None
        raise NotImplemented

    def insert(self, key, val) -> NoReturn:
        raise NotImplemented

    def remove(self, key) -> NoReturn:
        raise NotImplemented

    def has(self, key) -> NoReturn:
        raise NotImplemented

    def get(self, key):
        raise NotImplemented

    def __len__(self):
        raise NotImplemented
