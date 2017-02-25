import unittest
import sys

from garage import Garage
from sportcar import Sportcar
from van import Van
from truck import Truck

class TestCheckpointExcersise(unittest.TestCase):

    def setUp(self):
        self.sportcar = Sportcar("Lamborghini", "Diablo", 2000, "bloody red", 320)
        self.van = Van("GMC", "WTF1", 2016, "yellow", 1500)
        self.truck = Truck("Mercedes", "M45", 1997, "black", 8000, 8)

        self.garage = Garage(2, "New York")
        self.garage2 = Garage(6, "San Escobar")


    def test_sportcar_company(self):
        self.assertEqual("Lamborghini", self.sportcar.company)

    def test_sportcar_max_speed(self):
        self.assertEqual(320, self.sportcar.max_speed)

    def test_sportcar_displayed_info(self):
        msg = "bloody red Lamborghini Diablo, from 2000, max speed: 320 km/h"
        self.assertEqual(self.sportcar.display_info(), msg)

    def test_van_model(self):
        self.assertEqual("WTF1", self.van.model)

    def test_van_max_capacity(self):
        self.assertEqual(1500, self.van.max_capacity)

    def test_van_displayed_info(self):
        msg = "yellow GMC WTF1, from 2016, max capacity: 1500 kg"
        self.assertEqual(self.van.display_info(), msg)

    def test_truck_displayed_info(self):
        msg = "8-wheels black Mercedes M45, from 1997, max capacity: 8000 kg"
        self.assertEqual(self.truck.display_info(), msg)

    def test_garage_location(self):
        self.assertEqual("New York", self.garage.address)

    def test_garage_initial_capacity(self):
        self.assertEqual(2, self.garage.space_left())

    def test_garage_space_usage_vehicle_fits(self):
        self.garage.add_car(self.sportcar)
        self.assertEqual(1, self.garage.space_left())

    def test_garage_space_usage_vehicle_doesnt_fit(self):
        self.garage.add_car(self.truck)
        self.assertEqual(2, self.garage.space_left())

    def test_garage_display_vehicles(self):
        expected_string = "Cars available in New York:\n"\
                          "1. Bloody red Lamborghini Diablo, from 2000, max speed: 320 km/h\n" \
                          "2. Yellow GMC WTF1, from 2016, max capacity: 1500 kg\n" \
                          "3. 8-wheels black Mercedes M45, from 1997, max capacity: 8000 kg"

        self.garage2.add_car(self.sportcar)
        self.garage2.add_car(self.van)
        self.garage2.add_car(self.truck)

        self.garage2.display_vehicles()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, expected_string)

if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
