import unittest
import sys
import random
import string
import json
sys.path.insert(1, '../')
from app.api.distance import calculate_distance

class TestCalculateDistance(unittest.TestCase):
    def test_blank_address(self):
        """
        If address is blank then it will return invalid address
        """
        json = {'Address':'     '}
        result = calculate_distance(json)
        self.assertEqual(result, 'Invalid address')
        json = {'Address':''}
        result = calculate_distance(json)
        self.assertEqual(result, 'Invalid address')

    def test_mkad_address(self):
        """
        If address is MKAD then it will return
        'This address is located in the MKAD area'
        """
        json = {'Address':'MKAD'}
        result = calculate_distance(json)
        self.assertEqual(result, 'This address is located in the MKAD area')

    def test_random_address(self):
        """
        Random an address then it should return 'No result'
        With a specified address then it should return result which match the regex above
        """
        random_str_length = 10
        json = {'Address': ''.join((random.choice(string.ascii_lowercase) for x in range(random_str_length)))}
        result = calculate_distance(json)
        self.assertEqual(result, 'No result')
        json = {'Address': 'Ha Noi, Viet Nam'}
        result = calculate_distance(json)
        self.assertRegex(result, r'^[0-9]*.[0-9]*Km$')

if __name__ == '__main__':
    unittest.main()
