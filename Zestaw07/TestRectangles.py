import unittest
from rectangles import Rectangle
from points import Point


class TestFrac(unittest.TestCase):
    def test_print(self):
        self.assertEqual(str(Rectangle(0, 0, 1, 1)), "[(0, 0), (1, 1)]")
        self.assertEqual(str(Rectangle(5, 10, 15, 20)), "[(5, 10), (15, 20)]")
        self.assertEqual(repr(Rectangle(0, 0, 1, 1)), "Rectangle(0, 0, 1, 1)")
        self.assertEqual(repr(Rectangle(5, 10, 15, 20)), "Rectangle(5, 10, 15, 20)")

    def test_eq(self):
        self.assertTrue(Rectangle(1, 1, 2, 2) == Rectangle(1, 1, 2, 2))
        self.assertFalse(Rectangle(1, 1, 2, 2) == Rectangle(1, 0, 2, 2))
        self.assertFalse(Rectangle(1, 1, 2, 2) != Rectangle(1, 1, 2, 2))
        self.assertTrue(Rectangle(1, 1, 2, 2) != Rectangle(0, 1, 2, 2))

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).center(), Point(1, 1))
        self.assertEqual(Rectangle(0, 0, 3, 3).center(), Point(1.5, 1.5))
        self.assertEqual(Rectangle(1, 1, 3, 3).center(), Point(2, 2))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).area(), 4)
        self.assertEqual(Rectangle(0, 0, 5, 5).area(), 25)
        self.assertEqual(Rectangle(1, 1, 3, 3).area(), 4)

    def test_move(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).move(1, 1), Rectangle(1, 1, 3, 3))
        self.assertEqual(Rectangle(0, 0, 2, 2).move(2, 2), Rectangle(2, 2, 4, 4))
        self.assertEqual(Rectangle(0, 0, 2, 2).move(-2, -2), Rectangle(-2, -2, 0, 0))

    def test_intersection(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).intersection(Rectangle(1, 1, 2, 2)), Rectangle(1, 1, 2, 2))
        self.assertEqual(Rectangle(0, 0, 4, 4).intersection(Rectangle(-1, -1, 2, 2)), Rectangle(0, 0, 2, 2))

    def test_cover(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).cover(Rectangle(1, 1, 3, 3)), Rectangle(0, 0, 3, 3))
        self.assertEqual(Rectangle(0, 0, 4, 4).cover(Rectangle(-1, -1, 2, 2)), Rectangle(-1, -1, 4, 4))

    def test_make4(self):
        self.assertEqual(Rectangle(0, 0, 4, 4).make4(),  (Rectangle(0, 0, 2.0, 2.0), Rectangle(2.0, 0, 4, 2.0), Rectangle(0, 2.0, 2.0, 4), Rectangle(2.0, 2.0, 4, 4)))
        self.assertEqual(Rectangle(20, 20, 120, 120).make4(),  (Rectangle(20, 20, 70.0, 70.0), Rectangle(70.0, 20, 120, 70.0), Rectangle(20, 70.0, 70.0, 120), Rectangle(70.0, 70.0, 120, 120)))


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
