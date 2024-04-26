import unittest
from numbers_Ulam import numbers_Ulam

class TestNumbersUlam(unittest.TestCase):
    def test_numbers_Ulam_10(self):
        self.assertEqual(numbers_Ulam(10), [1, 2, 3, 4, 6, 8, 11, 13, 16, 18])

    def test_numbers_Ulam_2(self):
        self.assertEqual(numbers_Ulam(2), [1, 2])

    def test_numbers_Ulam_1(self):
        self.assertEqual(numbers_Ulam(1), [1])

    def test_numbers_Ulam_20(self):
        self.assertEqual(numbers_Ulam(20), [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69])

    def test_numbers_Ulam_5(self):
        self.assertEqual(numbers_Ulam(5), [1, 2, 3, 4, 6])

    def test_numbers_Ulam_30(self):
        self.assertEqual(numbers_Ulam(30), [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102, 106, 114, 126])

if __name__ == '__main__':
    unittest.main()