cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    '''Return a comma-separated list of cars of the Jeep model'''
    lst_out = []
    try:
        lst = cars.get('Jeep')
        lst_out = ','.join(lst)
        return lst_out
    except:
        return lst_out


def get_firstcar_all_manufacturer(cars=cars):
    '''Return a list of the first car of every Manufacturer'''
    lst_out = []
    try:
        for maker, car in cars.items():
            lst_out.append(car[0])
        return lst_out
    except:
        return lst_out


def get_all_vehicles_trail(cars=cars, grep='trail'):
    '''Return a list of cars with the string 'trail' (case-insensitive) attached to it'''
    '''https://stackoverflow.com/questions/18551458/how-to-frame-two-for-loops-in-list-comprehension-python'''
    lst_out = []
    try:
        lst_out = [vehicle for vehicles in cars.values() for vehicle in vehicles if 'trail' in vehicle.lower()]
        return lst_out
    except:
        lst_out


def sort_car_models(cars=cars):
    '''Return the dictionary of cars with all the models of the brands sorted alphabetically'''
    for brand, vehicles in cars.items():
        vehicles.sort()
        cars[brand] = vehicles
    return cars


print(get_all_jeeps())
print(get_firstcar_all_manufacturer())
print(get_all_vehicles_trail())
print(sort_car_models())