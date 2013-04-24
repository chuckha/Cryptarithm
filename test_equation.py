import unittest
from equation import Words, patterns, Numbers, generate_numbers

class GenerateNumbersTestCase(unittest.TestCase):
    def setUp(self):
        self.num_array = [0,1,2,3,4,5,6,7,8,9]

    def test_generate_number(self):
        self.assertEqual(generate_numbers(self.num_array, [[8,4,1,2]]), [8412])


class NumberTestCase(unittest.TestCase):
    
    def setUp(self):
        self.number = Numbers(8523, 5342, 2235)

    def test_pattern(self):
        self.assertEqual(self.number.patterns[0], [0,1,2,3])
        self.assertEqual(self.number.patterns[1], [1,3,4,2])
        self.assertEqual(self.number.patterns[2], [2,2,3,1])


class WordTestCase(unittest.TestCase):

    def setUp(self):
        self.words = Words("send", "more", "money")

    def test_pattern(self):
        self.assertEqual(self.words.patterns[0], [0,1,2,3])
        self.assertEqual(self.words.patterns[1], [4,5,6,1])
        self.assertEqual(self.words.patterns[2], [4,5,2,1,7])


if __name__ == '__main__':
    unittest.main()

