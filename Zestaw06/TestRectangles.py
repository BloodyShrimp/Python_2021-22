import unittest
from rectangles import Rectangle
from rectangles import Point


class TestTime(unittest.TestCase):

    def test_print(self):
        self.assertEqual(str(Rectangle(0, 0, 1, 1)), "[(0, 0), (1, 1)]")
        self.assertEqual(str(Rectangle(-5, 10, 0, -2)), "[(-5, 10), (0, -2)]")
        self.assertEqual(repr(Rectangle(0, 0, 1, 1)), "Rectangle(0, 0, 1, 1)")
        self.assertEqual(repr(Rectangle(-5, 10, 0, -2)), "Rectangle(-5, 10, 0, -2)")

    def test_eq(self):
        self.assertTrue(Rectangle(1, 1, 2, 2) == Rectangle(1, 1, 2, 2))
        self.assertFalse(Rectangle(1, 1, 2, 2) == Rectangle(1, 0, 2, 2))
        self.assertFalse(Rectangle(1, 1, 2, 2) != Rectangle(1, 1, 2, 2))
        self.assertTrue(Rectangle(1, 1, 2, 2) != Rectangle(0, 1, 2, 2))

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).center(), Point(1, 1))
        self.assertEqual(Rectangle(0, 0, 1, 1).center(), Point(0.5, 0.5))
        self.assertEqual(Rectangle(0, 0, 0, 0).center(), Point(0, 0))
        self.assertEqual(Rectangle(-2, -2, 2, 2).center(), Point(0, 0))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 1, 1).area(), 1)
        self.assertEqual(Rectangle(0, 0, 0, 0).area(), 0)
        self.assertEqual(Rectangle(-1, -1, 1, 1).area(), 4)
        self.assertEqual(Rectangle(-1, -3, 3, 1).area(), 16)

    def test_move(self):
        self.assertEqual(Rectangle(0, 0, 1, 1).move(1, 1), Rectangle(1, 1, 2, 2))
        self.assertEqual(Rectangle(0, 0, 0, 0).move(-2, -2), Rectangle(-2, -2, -2, -2))
        self.assertEqual(Rectangle(-1, -2, -3, -4).move(1, 1), Rectangle(0, -1, -2, -3))
        self.assertEqual(Rectangle(-1, -2, -3, -4).move(-1, -1), Rectangle(-2, -3, -4, -5))


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
