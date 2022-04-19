"""Task - 11.1. Город, страна"""
import unittest
from chapter_11.city_function import country_city


class TestCity(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(country_city('santiago', 'chile'),
                         '<<Santiago, Chile>>')


if __name__ == '__main__':
    unittest.main()
