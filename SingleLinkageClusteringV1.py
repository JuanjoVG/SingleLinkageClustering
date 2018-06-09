import math

from SingleLinkageClustering import SingleLinkageClustering


class SingleLinkageClusteringV1(SingleLinkageClustering):
    def nearest_clusters(self):
        min_distance = math.inf
        min_id1 = None
        min_id2 = None
        for id1 in self.clusters.keys():
            for id2 in self.clusters.keys():
                if id1 == id2:
                    continue
                distance = self.distance_between_clusters(id1, id2)
                if distance < min_distance:
                    min_distance = distance
                    min_id1 = id1
                    min_id2 = id2

        return min_id1, min_id2
