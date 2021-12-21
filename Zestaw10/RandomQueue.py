# zad 10.8

import random

class RandomQueue:

    def __init__(self, size = 10):
        self.size = size
        self.items = []

    def insert(self, item):
        if self.is_full():
            raise ValueError("Queue is full.")
        self.items.append(item)

    def remove(self):   # zwraca losowy element
        if self.is_empty():
            raise ValueError("Queue is empty.")
        index = random.randint(0, len(self.items) - 1)
        entry = self.items[index]
        self.items[index] = self.items[-1]
        del self.items[-1]
        return entry

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def clear(self):     # czyszczenie listy
        self.items.clear()