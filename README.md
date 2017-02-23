# Store your cars in OOP way!


## 1st part

### `Sportcar` class

##### `__init__`

Parameters:
* `size=1` - int, size of car
* `company` - string, car company
* `model` - string, car model
* `year` - integer, production year
* `color` - string, car color
* `max_speed` - integer, car's max speed in km/h

##### `display_info`

This function should __return__ full informations as a string in the following form:
`{color} {company} {model}, from {year}, max speed: {max_speed}`


### `Van` class

##### `__init__`

Parameters:
* `size=2` - int, size of car
* `company` - string, car company,
* `model` - string, car model
* `year` - integer, production year
* `color` - string, car color
* `max_capacity` - integer, car's max capacity in kg

##### `display_info`

This function should __return__ full informations as a string in the following form:
`{color} {company} {model}, from {year}, max capacity: {max_capacity}`


### `Truck` class

##### `__init__`

Parameters:
* `size=3` - int, size of car
* `company` - string, car company,
* `model` - string, car model
* `year` - integer, production year
* `color` - string, car color
* `max_capacity` - integer, car's max capacity in kg
* `wheel_count` - integer, number of wheels

##### `display_info`

This function should __return__ full informations as a string in the following form:
`{wheel_count}-wheels {color} {company} {model}, from {year}, max capacity: {max_capacity}`

### `Garage` class

##### `__init__`

Parameters:
* `space` - integer, space available in garage for variuos vehicles
* `addresses` - string, garage's address
* `vehicles` - list, collection of vehicles that are currently inside the garage

##### `add_car`
Adds given car to the list of vehicles

Parameters:
* `car` - `Sportcar` or `Van` or `Truck` object

Warning! Check available space before inserting car into given garage!

##### `space_left`
Function should print out information about available space in garage


# 2nd part

##### `display_vehicles`
Function should print out all vehicles' details (hint: use `display_info` from vehicles classes)


### `load_cars_from_csv`

Create `load_cars_from_csv` method in `Garage` class. It should take
1 parameter:

* `csv_path` - path to CSV file


First row in CSV file contains column headers

Warning! Let's assume we can insert cars as long as there is enough space in garage
