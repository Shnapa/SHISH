import unittest
from one_swap_sorting import one_swap_sorting

class TestOneSwapSorting(unittest.TestCase):

  def test_empty_sequence(self):
    self.assertEqual(one_swap_sorting([]), False)

  def test_single_element_sequence(self):
    self.assertEqual(one_swap_sorting([42]), False)

  def test_already_sorted_sequence(self):
    self.assertEqual(one_swap_sorting([0, 1, 2, 3]), False)

  def test_swap_sorts_sequence(self):
    self.assertEqual(one_swap_sorting([3, 2]), True)

  def test_swap_doesnt_sort_sequence(self):
    self.assertEqual(one_swap_sorting([2, 2]), False)

  def test_swap_sorts_with_multiple_disruptions(self):
    self.assertEqual(one_swap_sorting([5, 2, 3, 4, 1, 6]), True)

  def test_swap_sorts_with_disruptions_at_end(self):
    self.assertEqual(one_swap_sorting([1, 2, 3, 5, 4]), True)

  def test_no_element_to_swap_with(self):
    self.assertEqual(one_swap_sorting([1, 3, 2, 4]), True)
