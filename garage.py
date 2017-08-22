
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
        self.vehicles_list = []

    def add_car(self, car):
        if isinstance(car, Vehicle):
            if (self.space - car.size) >= 0:
                self.vehicles_list.append(car)
            else:
                raise OverflowError('There is no space for that vehicle!')
        else:
            raise TypeError('You can add only a vehicle!')

    def space_left(self):
        return self.space - sum([vehicle.size for vehicle in self.vehicles_list])

    def display_vehicles(self):
        vehicles_list_str = ''
        i = 1
        for vehicle in self.vehicles_list:
            vehicles_list_str += '{}. {}\n'.format(i, vehicle.display_info())
            i += 1
        return 'Cars available in {}:\n{}'.format(self.address, vehicles_list_str)

    @staticmethod
    def load_cars_from_csv(address, csv_path):

        with open(csv_path) as source:
            vehicle_list = csv.DictReader(source, delimiter='	')

            space = 0
            for vehicle in vehicle_list:
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

            for vehicle in vehicle_list:
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
