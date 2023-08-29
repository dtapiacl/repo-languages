import unittest

from fetch_languages import fetch_languages  # Make sure to import your function

class TestFetchLanguages(unittest.TestCase):
    
    def test_fetch_languages(self):
        # Replace 'lsst-it/lsst-control' with the target repository
        language_data = fetch_languages("lsst-it/lsst-control")
        
        # Test: Check if the function returns a dictionary
        self.assertIsInstance(language_data, dict)
        
        # Test: Check if the dictionary is not empty
        self.assertTrue(bool(language_data))

if __name__ == "__main__":
    unittest.main()
