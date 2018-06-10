import math


class Point:
    def __init__(self, id, coordinates):
        self.id = id
        self.coordinates = coordinates

    def distance(self, point):
        return math.sqrt(sum([(a - b) ** 2 for a, b in zip(self.coordinates, point.coordinates)]))

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False
