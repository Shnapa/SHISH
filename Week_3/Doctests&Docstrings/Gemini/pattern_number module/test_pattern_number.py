import unittest
from pattern_number import pattern_number

class TestPatternNumber(unittest.TestCase):

  def test_empty_sequence(self):
    self.assertEqual(pattern_number([]), None)

  def test_single_element_sequence(self):
    self.assertEqual(pattern_number([42]), None)

  def test_no_repeating_pattern(self):
    self.assertEqual(pattern_number([1, 2, 3]), None)

  def test_simple_repeating_pattern(self):
    self.assertEqual(pattern_number([1, 1]), ([1], 2))

  def test_longer_repeating_pattern(self):
    self.assertEqual(pattern_number([1, 2, 3, 1, 2, 3]), ([1, 2, 3], 2))

  def test_overlapping_repeating_pattern(self):
    self.assertEqual(pattern_number([1, 2, 1, 2, 3, 1, 2]), None)

  def test_uneven_repeating_pattern(self):
    self.assertEqual(pattern_number([1, 2, 3, 1, 2, 3, 1]), None)

  def test_repeated_sequence(self):
    self.assertEqual(pattern_number(list(range(10)) * 20), ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20))

  def test_string_with_repeating_pattern(self):
    self.assertEqual(pattern_number('hellohello'), ('hello', 2))

  def test_string_no_repeating_pattern(self):
    self.assertEqual(pattern_number('unique'), None)