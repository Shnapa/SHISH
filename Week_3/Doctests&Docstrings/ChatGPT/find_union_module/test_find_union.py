import unittest
from . import find_union

class TestFindUnion(unittest.TestCase):
    def test_both_strings(self):
        self.assertEqual(sorted(find_union("aaabb", "bbbbccc")), sorted('abc'))

    def test_mixed_case(self):
        self.assertEqual(sorted(find_union("aZAbc", "zzYYxp")), sorted('AYZabcpxz'))

    def test_non_string_input(self):
        self.assertIsNone(find_union("sfdfsdf", 2015))

    def test_empty_input(self):
        self.assertEqual(find_union("", ""), '')

    def test_one_empty_input(self):
        self.assertEqual(find_union("abc", ""), 'abc')
        self.assertEqual(find_union("", "xyz"), 'xyz')

    def test_duplicates(self):
        self.assertEqual(sorted(find_union("aabbcc", "ccbbaa")), sorted('abc'))

    def test_special_characters(self):
        self.assertEqual(sorted(find_union("!@#$", "$%^&*")), sorted('!@#$%^&*'))

if __name__ == '__main__':
    unittest.main()