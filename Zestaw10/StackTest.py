import unittest
from ArrayStack import Stack


class StackTest(unittest.TestCase):

    def test_push(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        with self.assertRaises(ValueError):
            stack.push(4)
        stack.pop()
        stack.push(4)
        with self.assertRaises(ValueError):
            stack.push(5)

    def test_pop(self):
        stack = Stack(3)
        stack.push(1)
        stack.pop()
        with self.assertRaises(ValueError):
            stack.pop()

    def test_is_full(self):
        stack = Stack(3)
        self.assertFalse(stack.is_full())
        stack.push(13)
        self.assertFalse(stack.is_full())
        stack.push(10)
        stack.push(2001)
        self.assertTrue(stack.is_full())

    def test_is_empty(self):
        stack = Stack(3)
        self.assertTrue(stack.is_empty())
        stack.push(5)
        self.assertFalse(stack.is_empty())
        stack.pop()
        self.assertTrue(stack.is_empty())


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy