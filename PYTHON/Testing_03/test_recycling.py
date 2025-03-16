
import unittest
from unittest.mock import Mock, patch

import recycling

class TestRecycling(unittest.TestCase):

    def test_max_values(self):
        
        # More than one house with the same max value

        example_data = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9]
        max_data = recycling.max_recycling(example_data)
        self.assertEqual(max_data.crates, 6)
        self.assertEqual(max_data.houses, [5, 7])

        # Single max value

        example_data = [1, 3, 9, 0, 2, 3, 3, 6]
        max_data = recycling.max_recycling(example_data)
        self.assertEqual(max_data.crates, 9)
        self.assertEqual(max_data.houses, [2])

    def test_min_values(self):
        
        # More than one joint min value

        example_data = [1, 2, 3, 0, 4, 5, 6, 7, 8, 0]
        min_data = recycling.min_recycling(example_data)
        self.assertEqual(min_data.crates, 0)
        self.assertEqual(min_data.houses, [1,4])

        # Single min value

        example_data = [1, 3, 9, 0, 2, 3, 3, 6]
        min_data = recycling.min_recycling(example_data)
        self.assertEqual(min_data.crates, 0)
        self.assertEqual(min_data.houses, [3])

    def test_total(self):
        
        example_data = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9]
        self.assertEqual(recycling.total_crates(example_data), 45)

    def test_get_crate_quantities(self):
        
        """Create a patch to replace the built in input function with a mock.
The mock is called mock_input, and we can change the way it behaves, e.g. provide
our desired return values. So when the code calls input(), instead of
calling the built-in input function, it will call the mock_input mock function,
which doesn't do anything except for returning the values provided in the
list of side_effect values - the first time it is called, it returns the first
side_effect value (1), second time it will return the second value, (3) etc..."""

        example_data = [1, 3, 9, 0, 2, 3, 3, 6]
        with patch('builtins.input', side_effect=example_data) as mock_input:
            self.assertEqual(recycling.get_crate_quantities(8), example_data)

    def test_int_input(self):
        
        # Test with some invalid input
        # put a valid input at the end or the function will never return

        with patch('builtins.input', side_effect=['a', 'b', 'c', '-2','-1000','123abc',
                                                   '1']) as mock_input:
            self.assertEqual(recycling.positive_int_input('example question'), 3)

        # ultimately, should return the valid calue at the end of the list.

        with patch('builtins.input', side_effect=['0', '13', '1', '100000']) as mock_input:
            self.assertEqual(recycling.positive_int_input('example question'), 1)
            self.assertEqual(recycling.positive_int_input('example question'), 13)
            self.assertEqual(recycling.positive_int_input('example question'), 1)
            self.assertEqual(recycling.positive_int_input('example question'), 100000)

    def test_main(self):

        with patch('builtins.input', side_effect=['4', '1', '2', '3', '4']) as mock_input:
            recycling.input = mock_input
            recycling.main()    # verify program doesn't crash :) Could also test thast it's 
            # printing correct data with a mock print function.


if __name__ == '__main__':
    unittest.main()

    
            