"""Task - 11.1. Город, страна"""
import unittest
from chapter_11.city_function import country_city


class TestCity(unittest.TestCase):
    def test_city_country(self):
        """Тест без населения"""
        self.assertEqual(country_city('santiago', 'chile'),
                         '<<Santiago, Chile>>')

    def test_city_country_population(self):
        """Тест с населением"""
        self.assertEqual(country_city('santiago', 'chile', population=5_000_000),
                         '<<Santiago, Chile - population 5000000>>')


if __name__ == '__main__':
    unittest.main()
