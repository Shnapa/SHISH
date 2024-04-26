import unittest
from one_swap_sorting import one_swap_sorting
class TestOneSwapSorting(unittest.TestCase):
    def test_sorted_sequence(self):
        self.assertFalse(one_swap_sorting([0, 1, 2, 3]))  # False
        self.assertFalse(one_swap_sorting([]))           # False
        self.assertFalse(one_swap_sorting([42]))         # False
    
    def test_single_swap(self):
        self.assertTrue(one_swap_sorting([3, 2]))  # True
        self.assertTrue(one_swap_sorting([5, 2, 3, 4, 1, 6]))  # True
        self.assertTrue(one_swap_sorting([1, 2, 3, 5, 4]))     # True
        self.assertTrue(one_swap_sorting([1, 3, 2]))  # True
    
    def test_no_single_swap(self):
        self.assertFalse(one_swap_sorting([2, 2]))  # False
        self.assertFalse(one_swap_sorting([1, 2, 3]))  # False
        self.assertFalse(one_swap_sorting([3, 1, 2]))  # False

if __name__ == '__main__':
    unittest.main()