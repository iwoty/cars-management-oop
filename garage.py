
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
