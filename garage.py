
from datetime import datetime
import csv

from vehicle import Vehicle
from sportcar import Sportcar
from van import Van
from truck import Truck


class Garage:

    def __init__(self, space, address):
        self.space = space
        self.address = address
        self.vehicles = []

    def add_car(self, car):
        if isinstance(car, Vehicle):
            if (self.space - car.size) >= 0:
                self.vehicles.append(car)
            else:
                raise OverflowError('There is no space for that vehicle!')
        else:
            raise TypeError('You can add only a vehicle!')

    def space_left(self):
        return self.space - sum([vehicle.size for vehicle in self.vehicles])

    def display_vehicles(self):
        vehicles_str = ''
        i = 1
        for vehicle in self.vehicles:
            vehicles_str += '{}. {}\n'.format(i, vehicle.display_info())
            i += 1
        return 'Cars available in {}:\n{}'.format(self.address, vehicles_str)

    @staticmethod
    def load_cars_from_csv(address, csv_path):

        with open(csv_path) as source:
            vehicles_list_csv = csv.DictReader(source, delimiter='	')

            space = 0
            for vehicle in vehicles_list_csv:
                if vehicle['type'] == 'sport':
                    space += 1
                elif vehicle['type'] == 'van':
                    space += 2
                elif vehicle['type'] == 'truck':
                    space += 3

            source.seek(0)
            # sets the iterator to beginning of the input file - otherwise
            # we cannot iterate one more time or we have to open file one more time

            new_garage = Garage(space, address)

            for vehicle in vehicles_list_csv:
                if vehicle['type'] == 'sport':
                    new_vehicle = Sportcar(vehicle['company'], vehicle['model'], vehicle['year'],
                                           vehicle['color'], vehicle['max_speed'])
                    new_garage.add_car(new_vehicle)

                elif vehicle['type'] == 'van':
                    new_vehicle = Van(vehicle['company'], vehicle['model'], vehicle['year'],
                                      vehicle['color'], vehicle['max_capacity'])
                    new_garage.add_car(new_vehicle)

                elif vehicle['type'] == 'truck':
                    new_vehicle = Truck(vehicle['company'], vehicle['model'], vehicle['year'],
                                        vehicle['color'], vehicle['max_capacity'], vehicle['wheel_count'])
                    new_garage.add_car(new_vehicle)

        return new_garage

    def get_average_age(self):
        current_year = datetime.now().year
        if self.vehicles:
            age_of_vehicles = [current_year - int(vehicle.year) for vehicle in self.vehicles]
            return sum(age_of_vehicles)/len(self.vehicles)

        else:
            return 0  # if a vehicle list is empty - average age is 0
