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

    def load_garage(self):
        from garage import Garage
        return Garage.load_cars_from_csv("Elk", "cars.csv")

    def test_01_sportcar_company(self):
        self.assertEqual("Lamborghini", self.get_sportcar().company)

    def test_02_sportcar_model(self):
        self.assertEqual("Diablo", self.get_sportcar().model)

    def test_03_sportcar_year(self):
        self.assertEqual(2000, self.get_sportcar().year)

    def test_04_sportcar_color(self):
        self.assertEqual("bloody red", self.get_sportcar().color)

    def test_05_sportcar_max_speed(self):
        self.assertEqual(320, self.get_sportcar().max_speed)

    def test_06_sportcar_displayed_info(self):
        msg = "bloody red Lamborghini Diablo, from 2000, max speed: 320 km/h"
        self.assertEqual(self.get_sportcar().display_info(), msg)

    def test_07_sportcar_size(self):
        self.assertEqual(1, self.get_sportcar().size)

    def test_08_van_model(self):
        self.assertEqual("WTF1", self.get_van().model)

    def test_09_van_max_capacity(self):
        self.assertEqual(1500, self.get_van().max_capacity)

    def test_10_van_size(self):
        self.assertEqual(2, self.get_van().size)

    def test_11_van_displayed_info(self):
        msg = "yellow GMC WTF1, from 2016, max capacity: 1500 kg"
        self.assertEqual(self.get_van().display_info(), msg)

    def test_12_truck_model(self):
        self.assertEqual("M45", self.get_truck().model)

    def test_13_truck_wheels(self):
        self.assertEqual(8, self.get_truck().wheel_count)

    def test_14_truck_size(self):
        self.assertEqual(3, self.get_truck().size)

    def test_15_truck_displayed_info(self):
        msg = "8-wheels black Mercedes M45, from 1997, max capacity: 8000 kg"
        self.assertEqual(self.get_truck().display_info(), msg)

    def test_16_garage_location(self):
        self.assertEqual("New York", self.get_garage1().address)

    def test_17_garage_initial_capacity(self):
        self.assertEqual(2, self.get_garage1().space_left())

    def test_18_garage_type_error(self):
        garage = self.get_garage1()
        with self.assertRaises(TypeError, msg="Test dupy się nie powiódł ;("):
            garage.add_car("dupa")

    def test_19_garage_space_usage_vehicle_fits(self):
        garage = self.get_garage1()
        garage.add_car(self.get_sportcar())
        self.assertEqual(1, garage.space_left())

    def test_20_garage_space_two_vehicles(self):
        garage2 = self.get_garage2()
        garage2.add_car(self.get_truck())
        garage2.add_car(self.get_truck())
        self.assertEqual(0, garage2.space_left())

    def test_21_garage_space_usage_vehicle_doesnt_fit(self):
        garage = self.get_garage1()
        with self.assertRaises(OverflowError, msg="This should not fit in here"):
            garage.add_car(self.get_truck())

# 2nd part

    def test_22_garage_display_vehicles(self):
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

    def test_23_load_cars_from_csv(self):
        expected_string = "Cars available in Elk:\n"\
                          "1. red Ferrari Diablo, from 2000, max speed: 350 km/h\n"\
                          "2. 10-wheels blue Scania OMG3, from 2010, max capacity: 10000 kg\n"\
                          "3. 8-wheels black Mercedes M45, from 1997, max capacity: 8000 kg\n"\
                          "4. yellow GMC WTF1, from 2016, max capacity: 2000 kg\n"\
                          "5. white Maserati Ghabi, from 2001, max speed: 299 km/h\n"

        garage = self.load_garage()
        actual_string = garage.display_vehicles()
        self.assertEqual(actual_string, expected_string)

    def test_24_load_cars_from_csv_space_left(self):
        garage = self.load_garage()
        self.assertEqual(0, garage.space_left(), msg="garage should be full")

    def test_25_average_age(self):
        garage2 = self.get_garage2()
        garage2.add_car(self.get_sportcar())
        garage2.add_car(self.get_van())

        self.assertEqual(9, garage2.get_average_age())

    def test_26_average_age_csv(self):
        garage = self.load_garage()
        self.assertEqual(12.2, garage.get_average_age())

    def test_27_average_age_zero(self):
        garage = self.get_garage1()
        self.assertEqual(0, garage.get_average_age())


if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False, verbosity=2)
