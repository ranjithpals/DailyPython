from FizzBuzz import fizzbuzz
import pytest


@pytest.mark.parametrize('num, ret', [
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz')
])
def test_fizzbuzz(num, ret):
    assert fizzbuzz(num) == ret
    # assert fizzbuzz(3) == 'Fizz'


#*******************************************************
# Run the test_fizzbuzz file from the CLI using 'pytest'
#*******************************************************


#if __name__ == "__main__":
    #test_fizzbuzz()