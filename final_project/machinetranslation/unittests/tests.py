import unittest

from translator import english_to_french, french_to_english


class englishToFrech(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french('none'),'')
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class frenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertNotEqual(french_to_english("Au revoir"),'')
        self.assertEqual(french_to_english('Bonjour'),'Hello')


unittest.main()