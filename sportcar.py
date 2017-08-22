
from vehicle import Vehicle


class Sportcar(Vehicle):

    def __init__(self, company, model, year, color, max_speed):
        super().__init__(company, model, year, color)
        self.max_speed = max_speed
        self.size = 1

    def display_info(self):
        return '{} {} {}, from {}, max speed: {} km/h'.format(self.color, self.company,
                                                              self.model, self.year, self.max_speed)
