
import unittest
from unittest.mock import patch
import camel

class TestCamelCase(unittest.TestCase):

    def test_capitalize(self):

        input_words = ['hello', 'WORLD', 'Camel', 'Case', '']
        capitalized = 'Hello', 'World', 'Camel', 'Case', ''

        for word in input_words:
            self.assertEqual(capitalized, camel.capitalize(word))

    def test_lower(self):
        # This isn't really needed, since we can assume that Python's library functions work correctly.
        input_words = ['hello', 'WORLD', 'Camel', 'Case', '']
        lower = 'hello', 'world', 'camel', 'case', ''