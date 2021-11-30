import unittest
import math
from circles import Circle
from points import Point


class TestFrac(unittest.TestCase):
    def test_print(self):
        self.assertEqual(str(Circle(0, 1, 5)), "Circle(0, 1, 5)")
        self.assertEqual(str(Circle(13, 10, 22)), "Circle(13, 10, 22)")
        self.assertEqual(repr(Circle(0, 1, 5)), "Circle(0, 1, 5)")
        self.assertEqual(repr(Circle(13, 10, 22)), "Circle(13, 10, 22)")

    def test_eq(self):
        self.assertTrue(Circle(0, 1, 5) == Circle(0, 1, 5))
        self.assertFalse(Circle(0, 1, 5) == Circle(13, 10, 22))
        self.assertFalse(Circle(0, 1, 5) != Circle(0, 1, 5))
        self.assertTrue(Circle(0, 1, 5) != Circle(13, 10, 22))

    def test_area(self):
        self.assertEqual(Circle(0, 1, 5).area(), math.pi * 5 ** 2)
        self.assertEqual(Circle(13, 1, 13).area(), math.pi * 13 ** 2)
        self.assertEqual(Circle(1, 1, 7).area(), math.pi * 7 ** 2)
        self.assertEqual(Circle(0, 0, 9).area(), math.pi * 9 ** 2)

    def test_move(self):
        self.assertEqual(Circle(1, 1, 5).move(8, 5), Circle(9, 6, 5))
        self.assertEqual(Circle(5, 2, 5).move(10, 13), Circle(15, 15, 5))
        self.assertEqual(Circle(1, 1, 5).move(-11, -11), Circle(-10, -10, 5))
        self.assertEqual(Circle(100, 50, 5).move(-100, -50), Circle(0, 0, 5))

    def test_cover(self):
        self.assertEqual(Circle(0, 0, 5).cover(Circle(1, -1, 3)), Circle(0, 0, 5))
        self.assertEqual(Circle(0, 0, 5).cover(Circle(5, 0, 6)), Circle(3, 0, 8))
        self.assertEqual(Circle(1, 3, 4).cover(Circle(8, 3, 2)), Circle(3.5, 3, 6.5))
        self.assertEqual(Circle(13, 5, 6).cover(Circle(3, 5, 3)), Circle(9.5, 5.0, 9.5))

if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
