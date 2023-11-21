import unittest
from fracs import *


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 2]), [1, 1])
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 4], [3, 8]), [5, 8])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 4], [3, 8]), [-1, 8])
        self.assertEqual(sub_frac([1, 5], [4, 6]), [-7, 15])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([1, 4], [3, 8]), [3, 32])
        self.assertEqual(mul_frac([3, 4], [5, 8]), [15, 32])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([1, 4], [3, 8]), [2, 3])
        self.assertEqual(div_frac([1, 2], [1, 2]), [1, 1])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertTrue(is_positive([-1, -2]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertFalse(is_zero([1, 2]))
        self.assertFalse(is_zero([6, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([3, 4]), 0.75)
        self.assertEqual(frac2float([3, 1]), 3)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()