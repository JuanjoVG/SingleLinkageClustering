import math

from versions.SingleLinkageClustering import SingleLinkageClustering


class SingleLinkageClusteringV2(SingleLinkageClustering):
    def nearest_clusters(self):
        min_distance = math.inf
        min_id1 = None
        min_id2 = None
        keys = list(self.clusters.keys())
        for i, id1 in enumerate(keys):
            for id2 in keys[i + 1:]:
                distance = self.distance_between_clusters(id1, id2)
                if distance < min_distance:
                    min_distance = distance
                    min_id1 = id1
                    min_id2 = id2

        return min_id1, min_id2
