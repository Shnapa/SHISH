import unittest
from turn_over import turn_over

class TestTurnOverFunction(unittest.TestCase):
    def test_positive_n(self):
        self.assertEqual(turn_over(3, [1, 2, 3, 4, 5]), [3, 2, 1, 4, 5])
        self.assertEqual(turn_over(2, ['a', 'b', 'c', 'd']), ['b', 'a', 'c', 'd'])

    def test_zero_n(self):
        self.assertEqual(turn_over(0, [1, 2, 3, 4, 5]), [])

    def test_negative_n(self):
        self.assertEqual(turn_over(-5, [1, 2, 3, 4, 5]), [])

    def test_empty_list(self):
        self.assertEqual(turn_over(3, []), [])
        self.assertEqual(turn_over(0, []), [])
        self.assertEqual(turn_over(-3, []), [])

    def test_n_greater_than_list_length(self):
        self.assertEqual(turn_over(7, [1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

if __name__ == "__main__":
    unittest.main()