import unittest
from translation import english_to_french
from translation import french_to_english


class TestTranslation(unittest.TestCase):
    def testEnglishToFrench(self):
        self.assertIsNotNone(english_to_french('Hello'))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('This is English'), 'Ceci est l\'anglais')
        self.assertEqual(english_to_french('Today in the News'), 'Aujourd\'hui dans l\'actualité')

    def testFrenchToEnglish(self):
        self.assertIsNotNone(french_to_english('Bonjour'))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Ceci est l\'anglais'), 'This is English')
        self.assertEqual(french_to_english('Aujourd\'hui dans l\'actualité'), 'Today in the News')


if __name__ == '__main__':
    unittest.main()
