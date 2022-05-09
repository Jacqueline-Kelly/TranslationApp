import unittest
from translator import *


class TestTranslator(unittest.TestCase):
    def test_en_2_fr_null(self):
        self.assertRaises(TypeError, lambda: english_to_french())
    
    def test_en_2_fr_hello(self):
        self.assertEqual('Bonjour', english_to_french('Hello'))
    
    def test_fr_2_en_null(self):
        self.assertRaises(TypeError, lambda: french_to_english())
    
    def test_fr_2_en_hello(self):
        self.assertEqual('Hello',  french_to_english('Bonjour'))


if __name__ == "__main__":
    unittest.main()