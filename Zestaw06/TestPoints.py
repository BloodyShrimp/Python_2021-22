import unittest
import math
from points import Point


class TestPoint(unittest.TestCase):

    def test_print(self):
        self.assertEqual(str(Point(1, 3)), "(1, 3)")
        self.assertEqual(str(Point(13, 10)), "(13, 10)")
        self.assertEqual(repr(Point(1, 3)), "Point(1, 3)")
        self.assertEqual(repr(Point(13, 10)), "Point(13, 10)")

    def test_eq(self):
        self.assertTrue(Point(1, 3) == Point(1, 3))
        self.assertFalse(Point(1, 3) == Point(5, 8))
        self.assertTrue(Point(1, 3) != Point(13, 3))
        self.assertFalse(Point(1, 3) != Point(1, 3))

    def test_add_point(self):
        self.assertEqual(Point(1, 3) + Point(1, 2), Point(2, 5))
        self.assertEqual(Point(1, 3) + Point(-1, -3), Point(0, 0))
        self.assertEqual(Point(-1, 3) + Point(1, 2), Point(0, 5))
        self.assertEqual(Point(0, 0) + Point(1, 1), Point(1, 1))

    def test_sub_point(self):
        self.assertEqual(Point(1, 3) - Point(1, 2), Point(0, 1))
        self.assertEqual(Point(1, 3) - Point(1, 3), Point(0, 0))
        self.assertEqual(Point(-1, 3) - Point(1, 2), Point(-2, 1))
        self.assertEqual(Point(0, 0) - Point(1, 1), Point(-1, -1))
        self.assertEqual(Point(1, 2) - Point(3, 4), Point(-2, -2))

    def test_mul_point(self):
        self.assertEqual(Point(1, 3) * Point(1, 2), 7)
        self.assertEqual(Point(1, 3) * Point(1, 3), 10)
        self.assertEqual(Point(-1, 3) * Point(1, 2), 5)
        self.assertEqual(Point(0, 0) * Point(1, 1), 0)

    def test_cross_point(self):
        self.assertEqual(Point(1, 3).cross(Point(1, 2)), -1)
        self.assertEqual(Point(1, 3).cross(Point(1, 3)), 0)
        self.assertEqual(Point(-1, 3).cross(Point(1, 2)), -5)
        self.assertEqual(Point(0, 0).cross(Point(1, 1)), 0)

    def test_length(self):
        self.assertEqual(Point(1, 3).length(), math.sqrt(10))
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertEqual(Point(10, 10).length(), math.sqrt(200))
        self.assertEqual(Point(3633, 4844).length(), 6055)


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy