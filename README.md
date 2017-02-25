# Store your cars in OOP way!


## 1st part

### `Sportcar` class
Please note, that every car of `Sportcar` type has a `size` instance attribute equals to `1`!


##### `__init__`

Parameters:
* `company` - string, car company
* `model` - string, car model
* `year` - integer, production year
* `color` - string, car color
* `max_speed` - integer, car's max speed in km/h

##### `display_info`

This function should __return__ full informations as a string in the following form:
`{color} {company} {model}, from {year}, max speed: {max_speed} km/h`



### `Van` class
Please note, that every car of `Van` type has a `size` instance attribute equals to `2`!


##### `__init__`

Parameters:
* `company` - string, car company,
* `model` - string, car model
* `year` - integer, production year
* `color` - string, car color
* `max_capacity` - integer, car's max capacity in kg

##### `display_info`

This function should __return__ full informations as a string in the following form:
`{color} {company} {model}, from {year}, max capacity: {max_capacity} kg`



### `Truck` class
Please note, that every car of `Truck` type has a `size` instance attribute equals to `3`!


##### `__init__`

Parameters:
* `company` - string, car company,
* `model` - string, car model
* `year` - integer, production year
* `color` - string, car color
* `max_capacity` - integer, car's max capacity in kg
* `wheel_count` - integer, number of wheels

##### `display_info`

This function should __return__ full informations as a string in the following form:
`{wheel_count}-wheels {color} {company} {model}, from {year}, max capacity: {max_capacity} kg`




### `Garage` class
Please note, that every garage should have a `vehicles` instance attribute - a list of vehicles stored inside.

##### `__init__`

Parameters:
* `space` - integer, space available in garage for various vehicles
* `addresses` - string, garage's address


##### `add_car`
Adds given car to the list of vehicles

Parameters:
* `car` - `Sportcar` or `Van` or `Truck` object

Warning! Check available space before inserting car into given garage!

##### `space_left`
Function should print out information about available space in garage.


# 2nd part

##### `display_vehicles`
Function should print out all vehicles' details.
Output should be like this:
```
Cars available in {location}:
1. {Color} {company} {model}, from {year}, max speed: {max_speed} km/h
2. {Color} {company} {model}, from {year}, max capacity: {max_capacity} kg
3. {Wheel_count}-wheels {color} {company} {model}, from {year}, max capacity: {max_capacity} kg
```

### `load_cars_from_csv`

Create `load_cars_from_csv` method in `Garage` class. It should take 1 parameter:

* `csv_path` - path to CSV file


First row in CSV file contains column headers

Warning! Let's assume we can insert cars as long as there is enough space in garage
