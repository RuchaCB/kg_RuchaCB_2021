"""To test all the functions from mapping.py"""
import unittest
from unittest.mock import patch
from mapping import mapping, validate

class TestMapping(unittest.TestCase):
    """To test the mapping.py"""
    def test_mapping(self):
        """To test the mapping() function"""
        self.assertEqual("true", mapping("abc", "bcd"))
        self.assertEqual("false", mapping("foo", "bar"))
        self.assertEqual("true", mapping("bar", "foo"))
        self.assertEqual("true", mapping("123123", "456456"))
        self.assertEqual("true", mapping("123", "abcdef"))
        self.assertEqual("false", mapping("123456", "123"))

    @patch('mapping.input', return_value='123 456 678')
    def test_validate(self, inp):
        """To test the validate() function"""
        self.assertEqual(validate(), 'Please enter a valid input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
