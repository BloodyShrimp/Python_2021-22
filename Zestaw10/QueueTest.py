import unittest
from ArrayQueue import Queue


class QueueTest(unittest.TestCase):

    def test_is_empty(self):
        queue = Queue(10)
        self.assertTrue(queue.is_empty())
        queue.put(1)
        self.assertFalse(queue.is_empty())
        queue.get()
        self.assertTrue(queue.is_empty())

    def test_is_full(self):
        queue = Queue(1)
        self.assertFalse(queue.is_full())
        queue.put(1)
        self.assertTrue(queue.is_full())
        queue.get()
        self.assertFalse(queue.is_full())

    def test_get(self):
        queue = Queue(10)
        with self.assertRaises(ValueError):
            queue.get()
        queue.put(1)
        self.assertEqual(queue.get(), 1)

    def test_put(self):
        queue = Queue(2)
        queue.put(1)
        queue.put(1)
        with self.assertRaises(ValueError):
            queue.put(1)


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
