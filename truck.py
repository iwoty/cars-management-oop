
from van import Van


class Truck(Van):

    def __init__(self, company, model, year, color, max_capacity, wheel_count):
        super().__init__(company, model, year, color, max_capacity)
        self.wheel_count = wheel_count
        self.size = 3
