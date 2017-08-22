
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
