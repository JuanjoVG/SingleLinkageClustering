import math

from SingleLinkageClustering import SingleLinkageClustering


class SingleLinkageClusteringV3(SingleLinkageClustering):
    def __init__(self, points):
        super().__init__(points)
        self.distance_matrix = self.compute_distance_matrix()

    def nearest_clusters(self):
        min_distance = math.inf
        min_id1 = None
        min_id2 = None

        for id1 in self.distance_matrix.keys():
            id1_distances = self.distance_matrix[id1]
            for id2 in id1_distances.keys():
                if id1 == id2:
                    continue
                distance = id1_distances[id2]
                if distance < min_distance:
                    min_distance = distance
                    min_id1 = id1
                    min_id2 = id2

        return min_id1, min_id2

    def compute_distance_matrix(self):
        matrix = {}
        keys = list(self.clusters.keys())
        for i, id1 in enumerate(keys):
            matrix[id1] = {}
            for id2 in keys:
                if id2 in matrix and id1 in matrix[id2]:
                    matrix[id1][id2] = matrix[id2][id1]
                else:
                    matrix[id1][id2] = self.distance_between_clusters(id1, id2)
        return matrix

    def clusterize(self, id1, id2):
        super().clusterize(id1, id2)
        dist_c1 = self.distance_matrix[id1]
        dist_c2 = self.distance_matrix[id2]
        self.distance_matrix[id1] = {k: min(v, dist_c2[k]) for k, v in dist_c1.items() if k in dist_c2}

        self.distance_matrix.pop(id2)
        for key in self.distance_matrix.keys():
            self.distance_matrix[key].pop(id2)
