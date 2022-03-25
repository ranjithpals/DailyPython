# Class for users of a social media platform

def users_list():
    users = [{'sno': 1, 'name': 'ranjith', 'age': 38, 'gender': 'M'},
             {'sno': 2, 'name': 'madhuri', 'age': 35, 'gender': 'F'},
             {'sno': 3, 'name': 'srinika', 'age': 6, 'gender': 'F'}]
    return users


def all_females():
    # sno_list = []
    return list(user['sno'] for user in users_list() if user['gender'] == 'F')


class Users:

    def __init__(self, user):
        self._sno = user.get('sno')
        self._name = user.get('name')
        self._age = user.get('age')
        self._gender = user.get('gender')


    def is_minor(self):
        if self._age < 18:
            return True
        else:
            return False

    def is_female(self):
        if self._gender == 'F':
            return True
        else:
            return False


if __name__ == '__main__':

    sample_user = {'sno': 1, 'name': "Srinika", 'age': 6, 'gender': 'F'}
    # new_user = Users(sample_user)
    print(all_females())