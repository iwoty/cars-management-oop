
from van import Van


class Truck(Van):

    def __init__(self, company, model, year, color, max_capacity, wheel_count):
        super().__init__(company, model, year, color, max_capacity)
        self.wheel_count = wheel_count
        self.size = 3

    def display_info(self):
        return '{}-wheels {} {} {}, from {}, max capacity: {} kg'.format(self.wheel_count, self.color, self.company,
                                                                         self.model, self.year, self.max_capacity)
