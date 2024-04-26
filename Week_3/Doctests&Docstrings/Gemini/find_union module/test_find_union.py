import unittest
from find_union import find_union

class TestFindUnion(unittest.TestCase):

  def test_empty_strings(self):
    self.assertEqual(find_union("", ""), "")

  def test_single_letter_strings(self):
    self.assertEqual(find_union("a", ""), "a")
    self.assertEqual(find_union("", "b"), "b")

  def test_all_uppercase(self):
    self.assertEqual(find_union("HELLO", "WORLD"), "DEHLORW")

  def test_all_lowercase(self):
    self.assertEqual(find_union("hello", "world"), "dehlorw")

  def test_mixed_case(self):
    self.assertEqual(find_union("Hello", "World"), "HWdelor")

  def test_duplicate_letters(self):
    self.assertEqual(find_union("aaabb", "bbbbccc"), "abc")

  def test_non_string_arguments(self):
    self.assertEqual(find_union("hello", 123), None)
    self.assertEqual(find_union(456, "world"), None)