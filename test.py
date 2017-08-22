import unittest
import sys


class TestCheckpointExcersise(unittest.TestCase):

    def get_sportcar(self):
        from sportcar import Sportcar
        return Sportcar("Lamborghini", "Diablo", 2000, "bloody red", 320)

    def get_van(self):
        from van import Van
        return Van("GMC", "WTF1", 2016, "yellow", 1500)

    def get_truck(self):
        from truck import Truck
        return Truck("Mercedes", "M45", 1997, "black", 8000, 8)

    def get_garage1(self):
        from garage import Garage
        return Garage(2, "New York")

    def get_garage2(self):
        from garage import Garage
        return Garage(6, "San Escobar")

    def test_01_sportcar_company(self):
        self.assertEqual("Lamborghini", self.get_sportcar().company)

    def test_02_sportcar_max_speed(self):
        self.assertEqual(320, self.get_sportcar().max_speed)

    def test_03_sportcar_displayed_info(self):
        msg = "bloody red Lamborghini Diablo, from 2000, max speed: 320 km/h"
        self.assertEqual(self.get_sportcar().display_info(), msg)

    def test_04_van_model(self):
        self.assertEqual("WTF1", self.get_van().model)

    def test_05_van_max_capacity(self):
        self.assertEqual(1500, self.get_van().max_capacity)

    def test_06_van_displayed_info(self):
        msg = "yellow GMC WTF1, from 2016, max capacity: 1500 kg"
        self.assertEqual(self.get_van().display_info(), msg)

    def test_07_truck_displayed_info(self):
        msg = "8-wheels black Mercedes M45, from 1997, max capacity: 8000 kg"
        self.assertEqual(self.get_truck().display_info(), msg)

    def test_08_garage_location(self):
        self.assertEqual("New York", self.get_garage1().address)

    def test_09_garage_initial_capacity(self):
        self.assertEqual(2, self.get_garage1().space_left())

    def test_10_garage_space_usage_vehicle_fits(self):
        garage = self.get_garage1()
        garage.add_car(self.get_sportcar())
        self.assertEqual(1, garage.space_left())

    def test_11_garage_space_usage_vehicle_doesnt_fit(self):
        garage = self.get_garage1()
        garage.add_car(self.get_truck())
        self.assertEqual(2, garage.space_left())

    def test_12_garage_display_vehicles(self):
        expected_string = "Cars available in San Escobar:\n"\
                          "1. bloody red Lamborghini Diablo, from 2000, max speed: 320 km/h\n" \
                          "2. yellow GMC WTF1, from 2016, max capacity: 1500 kg\n" \
                          "3. 8-wheels black Mercedes M45, from 1997, max capacity: 8000 kg\n"

        garage2 = self.get_garage2()
        garage2.add_car(self.get_sportcar())
        garage2.add_car(self.get_van())
        garage2.add_car(self.get_truck())

        actual = garage2.display_vehicles()
        self.assertEqual(actual, expected_string)

if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False, verbosity=2)
