import unittest

class TestTranslate(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")    

if __name__ == "__main__":
    unittest.main()