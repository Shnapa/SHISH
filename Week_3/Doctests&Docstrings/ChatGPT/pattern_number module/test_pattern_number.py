import unittest
from pattern_number import pattern_number

class TestPatternNumber(unittest.TestCase):

    def test_empty_sequence(self):
        self.assertIsNone(pattern_number([]))

    def test_single_element_sequence(self):
        self.assertIsNone(pattern_number([42]))

    def test_two_element_sequence(self):
        self.assertIsNone(pattern_number([1, 2]))

    def test_identical_elements(self):
        self.assertEqual(pattern_number([1, 1]), ([1], 2))

    def test_no_repeating_pattern(self):
        self.assertIsNone(pattern_number([1, 2, 1]))

    def test_repeating_pattern(self):
        self.assertEqual(pattern_number([1, 2, 3, 1, 2, 3]), ([1, 2, 3], 2))

    def test_incomplete_pattern(self):
        self.assertIsNone(pattern_number([1, 2, 3, 1, 2]))

    def test_incomplete_repeating_pattern(self):
        self.assertIsNone(pattern_number([1, 2, 3, 1, 2, 3, 1]))

    def test_long_sequence(self):
        self.assertEqual(pattern_number(list(range(10)) * 20), (list(range(10)), 20))

    def test_string_input_identical_characters(self):
        self.assertEqual(pattern_number('HelloHello'), ('Hello', 2))

    def test_string_input_no_pattern(self):
        self.assertIsNone(pattern_number('ThisIsATest'))

if __name__ == '__main__':
    unittest.main()