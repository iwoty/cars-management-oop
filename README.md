# Store your cars in OOP way!
You'll implement classes that will help us manage company's car fleet.

# Specification
Below you'll find specifications of classes that you should implement in order to pass the tests. Have in mind that this specification does not contain implementation details. **It is your responsibility to decide which methods/variables should be static or where to use inheritance and etc.** Remember that you can implement more classes to make your code better.

Specification is divided into two parts. Both parts are mandatory, but you have to implement them in given order.

## General rules
* do not modify cars.csv file because you might break the tests
* you don't have to write docstrings during this assignment because time is short
* even though you work alone please commit often and properly, make pushes after each part of the exercise
* test your code often
* pay attention to csv file delimiter

## 1st part

### `Sportcar` class
Please note, that every car of `Sportcar` type has a `size` attribute equal to `1`!


##### `__init__`

Parameters:
* `company` - string, car company
* `model` - string, car model
* `year` - integer, production year
* `color` - string, car color
* `max_speed` - integer, car's max speed in km/h

##### `display_info`

This method should __return__ full informations as a string in the following form:
`{color} {company} {model}, from {year}, max speed: {max_speed} km/h`



### `Van` class
Please note, that every car of `Van` type has a `size` attribute equal to `2`!


##### `__init__`

Parameters:
* `company` - string, car company,
* `model` - string, car model
* `year` - integer, production year
* `color` - string, car color
* `max_capacity` - integer, car's max capacity in kg

##### `display_info`

This method should __return__ full informations as a string in the following form:
`{color} {company} {model}, from {year}, max capacity: {max_capacity} kg`



### `Truck` class
Please note, that every car of `Truck` type has a `size` attribute equal to `3`!


##### `__init__`

Parameters:
* `company` - string, car company,
* `model` - string, car model
* `year` - integer, production year
* `color` - string, car color
* `max_capacity` - integer, car's max capacity in kg
* `wheel_count` - integer, number of wheels

##### `display_info`

This method should __return__ full informations as a string in the following form:
`{wheel_count}-wheels {color} {company} {model}, from {year}, max capacity: {max_capacity} kg`




### `Garage` class
Please note, that every garage should have a `vehicles` instance attribute - a list of vehicles stored inside.

##### `__init__`

Parameters:
* `space` - integer, space available in garage for various vehicles
* `address` - string, garage's address


##### `add_car`
Adds given car to the list of vehicles

Parameters:
* `car` - `Sportcar` or `Van` or `Truck` object. Raises TypeError when something else is added.

Warning! Check available space before inserting car into given garage! If there is no space an `OverflowError` should be raised.

##### `space_left`
Method should return information about available space in garage.


# 2nd part

##### `display_vehicles`
Method should retrurn all vehicles' details.
Output should be like this:
```
Cars available in {location}:
1. {Color} {company} {model}, from {year}, max speed: {max_speed} km/h
2. {Color} {company} {model}, from {year}, max capacity: {max_capacity} kg
3. {Wheel_count}-wheels {color} {company} {model}, from {year}, max capacity: {max_capacity} kg
```

#### `load_cars_from_csv`
Create `load_cars_from_csv` method in `Garage` class. It should take 2 parameters:

* `address` - garage's address
* `csv_path` - path to CSV file

This method should return `Garage object`. The space of garage is equal to the amount of cars in CSV file.

First row in CSV file contains column headers

#### `get_average_age`
This method should return average age of cars in a garage.
