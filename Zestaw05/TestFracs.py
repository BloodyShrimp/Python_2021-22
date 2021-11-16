import unittest
import fracs


class TestFractions(unittest.TestCase):

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([0, 8], [14, 3]), [14, 3])
        self.assertEqual(fracs.add_frac([-1, 13], [2, 26]), [0, 1])
        self.assertEqual(fracs.add_frac([236, 12], [189, 468]), [3131, 156])
        self.assertEqual(fracs.add_frac([67, 100], [33, 100]), [1, 1])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([5, 7], [5, 7]), [0, 1])
        self.assertEqual(fracs.sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.sub_frac([0, 100], [3, 7]), [-3, 7])
        self.assertEqual(fracs.sub_frac([168, 246], [135, 57]), [-1313, 779])
        self.assertEqual(fracs.sub_frac([5, 7], [0, 7]), [5, 7])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(fracs.mul_frac([0, 2], [1, 3]), [0, 1])
        self.assertEqual(fracs.mul_frac([18, 3], [6, 9]), [4, 1])
        self.assertEqual(fracs.mul_frac([1, 2], [0, 3]), [0, 1])
        self.assertEqual(fracs.mul_frac([98, -13], [-468, 85]), [3528, 85])
        self.assertEqual(fracs.mul_frac([-1, -5], [14, -7]), [-2, 5])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([1, 10], [5, 6]), [3, 25])
        self.assertEqual(fracs.div_frac([0, 2], [1, 3]), [0, 1])
        self.assertEqual(fracs.div_frac([1, 3], [1, 6]), [2, 1])
        self.assertEqual(fracs.div_frac([5, -2], [17, 3]), [-15, 34])
        self.assertEqual(fracs.div_frac([469, 26], [1679, 986]), [231217, 21827])

    def test_is_positive(self):
        self.assertEqual(fracs.is_positive([1, 2]), True)
        self.assertEqual(fracs.is_positive([-1, 2]), False)
        self.assertEqual(fracs.is_positive([0, 5]), False)
        self.assertEqual(fracs.is_positive([17, 9]), True)
        self.assertEqual(fracs.is_positive([-7, -13]), True)
        self.assertEqual(fracs.is_positive([20, -10]), False)

    def test_is_zero(self):
        self.assertEqual(fracs.is_zero([0, 2]), True)
        self.assertEqual(fracs.is_zero([1, 2]), False)
        self.assertEqual(fracs.is_zero([0, 0]), True)
        self.assertEqual(fracs.is_zero([2, 0]), False)

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(fracs.cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(fracs.cmp_frac([1, 3], [1, 3]), 0)
        self.assertEqual(fracs.cmp_frac([1, 2], [-1, 3]), 1)
        self.assertEqual(fracs.cmp_frac([-168, 13], [189, 59]), -1)
        self.assertEqual(fracs.cmp_frac([168, 13], [189, 59]), 1)
        self.assertEqual(fracs.cmp_frac([0, 2], [1, 3]), -1)
        self.assertEqual(fracs.cmp_frac([0, 2], [-1, 3]), 1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([0, 2]), 0)
        self.assertEqual(fracs.frac2float([5, 5]), 1)
        self.assertEqual(fracs.frac2float([45, 90]), 0.5)
        self.assertEqual(fracs.frac2float([6, 9]), 0.6666666666666666)
        self.assertEqual(fracs.frac2float([25, 2]), 12.5)
        self.assertEqual(fracs.frac2float([25, 3]), 8.3333333333333333)


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy