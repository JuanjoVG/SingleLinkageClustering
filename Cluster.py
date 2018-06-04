import math


class Cluster:
    def __init__(self, id, points):
        self.id = id
        self.points = points

    def merge(self, cluster):
        self.points += cluster.points

    def distance(self, cluster):
        min_dist = math.inf
        for p1 in self.points:
            for p2 in cluster.points:
                distance = p1.distance(p2)
                if distance < min_dist:
                    min_dist = distance
        return min_dist

    def __repr__(self):
        return str([str(p.id) for p in self.points])
