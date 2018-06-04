import math


class Point:
    def __init__(self, id, coordinates):
        self.id = id
        self.coordinates = coordinates

    def distance(self, point):
        return math.sqrt(sum([(a - b) ** 2 for a, b in zip(self.coordinates, point.coordinates)]))
