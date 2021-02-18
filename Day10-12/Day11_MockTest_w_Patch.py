# Import class to be Tested
from classUsers import Users, all_females, users_list

# Import the Testing modules to create Mock Test
import unittest
from mock import Mock, patch


class TestUser(unittest.TestCase):

    # setUp Method will override the method in the TestCase class
    def setUp(self):
        # Initialize the User Class
        self._sno = 1
        self._name = 'Srinika'
        self._age = 7
        self._gender = 'F'

    def test_is_minor(self):
        # Validate the is_minor function
        user = Mock()
        # user.sno = self._sno
        user._sno = self._name
        user._age = self._age
        # user.gender = self._gender

        # Here we DON'T need to exactly instantiate the User class
        # Need to mock the User class object with just the attribute needed to implement the function
        # Here only age property is needed to Implement the is_minor Method.
        output = Users.is_minor(user)
        # Validate the Output
        self.assertTrue(output)


    def test_is_female(self):

        # Here 'mock_all_females' is going to mock (act as) users_list function in classUsers Module
        with patch('classUsers.users_list') as mocked_users_list:
            mocked_users_list.return_value = [
                {'sno': 1, 'name': 'ranjith', 'age': 38, 'gender': 'M'},
                {'sno': 2, 'name': 'madhuri', 'age': 35, 'gender': 'F'},
                {'sno': 3, 'name': 'srinika', 'age': 6, 'gender': 'F'}]

            # Validate the is_gender function
            # When the all_females function is executed the mocked_users_list is used in the place of users_list()
            output = all_females()
            print(output)
            self.assertEquals(output, [2, 3])


if __name__ == '__main__':
    unittest.main()


