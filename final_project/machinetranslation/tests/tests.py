import unittest
from translator import french_2_english, english_2_french


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertRaises(TypeError, french_2_english) 
        self.assertEqual(french_2_english('Bonjour'), 'Hello')


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertRaises(TypeError, english_2_french)
        self.assertEqual(english_2_french('Hello'), 'Bonjour')

unittest.main()