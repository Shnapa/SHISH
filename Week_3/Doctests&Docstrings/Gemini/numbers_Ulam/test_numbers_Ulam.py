import unittest
from numbers_Ulam import numbers_Ulam

class TestNumbersUlam(unittest.TestCase):

  def test_n_equals_1(self):
    self.assertEqual(numbers_Ulam(1), [1])

  def test_n_equals_2(self):
    self.assertEqual(numbers_Ulam(2), [1, 2])

  def test_n_equals_10(self):
    self.assertEqual(numbers_Ulam(10), [1, 2, 3, 4, 6, 8, 11, 13, 16, 18])

  def test_n_greater_than_2(self):
    self.assertEqual(numbers_Ulam(5), [1, 2, 3, 4, 6])

  def test_zero_or_negative_n(self):
    self.assertEqual(numbers_Ulam(0), [])
    self.assertEqual(numbers_Ulam(-2), [])