import unittest
from turn_over import turn_over


class TestTurnOver(unittest.TestCase):

  def test_reverse_specific_number(self):
    self.assertEqual(turn_over(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l']), ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l'])

  def test_reverse_all_items(self):
    self.assertEqual(turn_over(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

  def test_reverse_more_than_list_length(self):
    self.assertEqual(turn_over(15, [1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

  def test_handle_empty_list(self):
    self.assertEqual(turn_over(3, []), [])

  def test_handle_zero_reverse(self):
    self.assertEqual(turn_over(0, [1, 2, 3]), [1, 2, 3])