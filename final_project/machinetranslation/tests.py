import unittest

from translator import english_to_french, french_to_english

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english('None'), ' ')
    def test2(self):
        self.assertNotEqual(french_to_english(0), 0)
    def test3(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test4(self):
        self.assertEqual(french_to_english('Salut'), 'Hi')

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french('None'), ' ')
    def test2(self):
        self.assertNotEqual(english_to_french(0), 0)
    def test3(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test4(self):
        self.assertEqual(english_to_french('Hi'), 'Salut')

unittest.main()