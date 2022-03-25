# Import the random_sum Module, related functions
from random_sum import sum_of_numbers_randint_list, sum_of_two_numbers, print_text

# Import Mock and Patch functions
import unittest
from mock import Mock, patch


class TestApp(unittest.TestCase):

    # Test the sum_of_numbers_randint_list function
    # Here is the patch function is used as a decorator which mocks the random.randint function
    # random.randint is used in the 'sum_of_numbers_randint_list' function of random_sum.py module
    # The name of the mocked function is passed as an parameter to the test function
    # This is also equivalent to 'with patch('random.randint') as mocked_random_int:'
    # Inside the test function we define the return value of the mocked_random_int as 17
    # So the random.randint always returns the same number, which makes it easy to test
    @patch('random.randint')
    def test_sum_of_numbers_randint_list(self, mocked_random_int):
        sample_lst = [1, 2]
        # First instance of the test
        mocked_random_int.return_value = 17
        self.assertEqual(sum_of_numbers_randint_list(sample_lst), 20)
        self.assertTrue(mocked_random_int.called)
        mocked_random_int.assert_called_with(1, 100)

        # Second instance of the test
        mocked_random_int.return_value = 10
        self.assertEqual(sum_of_numbers_randint_list(sample_lst), 13)
        self.assertTrue(mocked_random_int.called)
        mocked_random_int.assert_called_with(1, 100)

    @patch('random_sum.print_text')
    def test_sum_of_two_numbers(self, mocked_print_text):
        # making sure mocked print_text function is called properly
        sum_of_two_numbers(3, 4)
        self.assertTrue(mocked_print_text.called)
        mocked_print_text.assert_called_with(7)


if __name__ == "__main__":
    unittest.main()