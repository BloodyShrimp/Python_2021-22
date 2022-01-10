import unittest
import math
import median_mode

class TestFrac(unittest.TestCase):
    def test_median(self):
        self.assertEqual(median_mode.mediana_sort([1, 2, 3, 4], 0, 3), 2.5)
        self.assertEqual(median_mode.mediana_sort([1, 2, 3, 4, 5], 0, 4), 3)
        self.assertEqual(median_mode.mediana_sort([5, 3, 1, 2, 4], 0, 4), 3)
        self.assertEqual(median_mode.mediana_sort([123, 256, 324, 4, 5], 0, 2), 256)
        self.assertEqual(median_mode.mediana_sort([123, 256, 324, 4, 5], 0, 4), 123)
        self.assertEqual(median_mode.mediana_sort([123, 256, 324, 4, 5], 1, 4), 130.5)

    def test_mode(self):
        self.assertEqual(median_mode.moda_sort([1, 2, 3, 4], 0, 3), None)
        self.assertEqual(median_mode.moda_sort([1, 2, 1, 3, 4], 0, 4), 1)
        self.assertEqual(median_mode.moda_sort([89, 156, 13, 66, 13, 2, 133, 13, 1345, 200, 13, 133, 133], 0, 12), 13)
        self.assertEqual(median_mode.moda_sort([89, 156, 13, 66, 13, 2, 133, 13, 1345, 200, 13, 133, 133], 5, 12), 133)

if __name__ == '__main__':
    unittest.main()
