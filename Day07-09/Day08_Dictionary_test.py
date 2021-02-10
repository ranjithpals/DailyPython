import Day08_Dictionary_challenge as Module

'''
https://www.tutorialsteacher.com/python/python-assert
https://dbader.org/blog/python-assert-tutorial
'''

def test_get_all_jeeps():
    '''Test the get_all_jeeps function of the Day08_Dictionary_challenge module'''
    expected = 'Grand Cherokee,Cherokee,Trailhawk,Trackhawk'
    actual = Module.get_all_jeeps()
    assert expected == actual


def test_get_firstcar_all_manufacturer():
    '''Test the get_firstcar_all_manufacturer function of the Day08_Dictionary_challenge module'''
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    actual = Module.get_firstcar_all_manufacturer()
    assert expected == actual


def test_get_all_vehicles_trail():
    '''Test the get_all_vehicles_trail function of the Day08_Dictionary_challenge module'''
    expected = ['Trailblazer', 'Trailhawk']
    actual = Module.get_all_vehicles_trail()
    assert expected == actual


def test_sort_car_models():
    '''Test the sort_car_models function of the Day08_Dictionary_challenge module'''
    expected = {'Foord': ['Fairlane', 'Falcon', 'Festiva', 'Focus'], 'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'], 'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'], 'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'], 'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk']}
    actual = Module.sort_car_models()
    assert expected == actual, 'Test Failed: test_sort_car_models, Result does not match the Expected'


if __name__ == "__main__":

    test_get_all_jeeps()
    test_get_firstcar_all_manufacturer()
    test_get_all_vehicles_trail()
    try:
        test_sort_car_models()
    except Exception as msg:
        print(msg)



