
from vehicle import Vehicle


class Van(Vehicle):

    def __init__(self, company, model, year, color, max_capacity):
        super().__init__(company, model, year, color)
        self.max_capacity = max_capacity
        self.size = 2
