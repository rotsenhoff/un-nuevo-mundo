
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
        lower = 'hello', 'world', 'camel', 'case',

        for word in input_words:
            self.assertEqual(lower, camel.lowercase(word))

    def test_camel_case_single_words(self):

        input_and_expected_outputs = {
            'hello': 'hello',
            'WORLD': 'world',
            'Camel': 'camel',
            'Case': 'case',
            '': ''
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_uppercase(self):

        input_and_expected_outputs = {
            'hello world': 'helloWorld',
            'HELLO WORLD': 'helloWorld',
            'Camel Case': 'camelCase',
            '': ''
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_lowercase(self):

        input_and_expected_outputs = {
            'hello': 'hello',
            'heLLO': 'hello',
            'camel case': 'camelCase'}
        
        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_many_words(self):

        input_and_expected_outputs = {
            'hello world': 'helloWorld',
            'HELLO WORLD': 'helloWorld',
            'Camel Case': 'camelCase',
            'this is a sentence': 'thisIsASentence',
            
            '': ''
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_with_extra_spaces(self):

        input_and_expected_outputs = {
            ' hello world': 'helloWorld',
            'HELLO WORLD ': 'helloWorld',
            ' Camel Case ': 'camelCase',
            '\tThere is a \t tab here': 'thereIsATabHere',
            ' this is a sentence ': 'thisIsASentence',
            '': ''
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_with_emojis(self):
        
        input_and_expected_outputs = {
            '😂😂😂😂😂': '😂😂😂😂😂',
            '😂😂😂😂😂😂': '😂😂😂😂😂😂',
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_international(self):

        input_and_expected_outputs = {
            'Write a résumé': 'writeARésumé',
            'Über die Brücke': 'überDieBrücke',
            'Fahren Sie nach Hause': 'fahrenSieNachHause',
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_input_and_output(self):

        # Patch the input. using with context manager automatically takes care of unpatching.

        with patch('builtins.input', return_value='This IS another SENTenCE'):

            # And, patch the output
            with patch('builtins.print') as mock_print:

                camel.main()
                mock_print.assert_called_with('this ISAnotherSentence')

if __name__ == '__main__':
    unittest.main()

    