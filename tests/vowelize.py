import unittest
from vowelize import vowelize

class TestStringMethods(unittest.TestCase):

    def test_leading_y(self):
        self.assertEqual(vowelize("YOGHURT"), 2)
        
    def test_trailing_y(self):
        self.assertEqual(vowelize("TURKEY"), 3)
        self.assertEqual(vowelize("MOSTLY"), 2)
        
    def test_consonant_y(self):
        self.assertEqual(vowelize("UNMYELINATED"), 5)
        self.assertEqual(vowelize("MYOPIC"), 2)

    def test_pure_vowel_y(self):
        self.assertEqual(vowelize("BICYCLE"), 3)
        self.assertEqual(vowelize("POLYMER"), 3)
        self.assertEqual(vowelize("LYMPH"), 1)
        self.assertEqual(vowelize("GYM"), 1)

    def test_vowels(self):
        self.assertEqual(vowelize("MR"), 0)
        self.assertEqual(vowelize("DUDE"), 2)
        self.assertEqual(vowelize("FOOD"), 2)
        self.assertEqual(vowelize("OVERFLOW"), 3)
        self.assertEqual(vowelize("CAT"), 1)

if __name__ == '__main__':
    unittest.main()
