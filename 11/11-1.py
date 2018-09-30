import unittest
from city_functions import describe_city


class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country = describe_city("guangzhou", "china", 5000)
        self.assertEqual(city_country, "Guangzhou,China-population 5000")


if __name__ == '__main__':
    city_case = CityTestCase()
    city_case.test_city_country()
