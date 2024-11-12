import unittest
import convert


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_str_to_float_1(self):
        input = "17.6"
        expected = 17.6
        actual = convert.str_to_float(input)
        self.assertEqual(expected, actual)
    def test_str_to_float_2(self):
        input = "hello"
        expected = None
        actual = convert.str_to_float(input)
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()

