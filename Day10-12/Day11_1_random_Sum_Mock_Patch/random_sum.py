import random

lst = [1, 2]


# Function to add a random number between 1, 100 to sum of a list.
def sum_of_numbers_randint_list(i_lst=None):

    total = sum(i_lst)
    total += random.randint(1, 100)
    return total

# Adding two more functions


# Function to print some text
def print_text(text):
    print(text)


# Function to add two numbers
def sum_of_two_numbers(number1, number2):
    total = number1 + number2
    print_text(total)
    return total


if __name__ == "__main__":
    print(sum_of_numbers_randint_list([1, 2]))
    sum_of_two_numbers(3, 4)