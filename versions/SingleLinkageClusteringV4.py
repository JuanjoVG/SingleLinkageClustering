import math

from classes.Bucket import Bucket
from versions.SingleLinkageClustering import SingleLinkageClustering


class SingleLinkageClusteringV4(SingleLinkageClustering):
    def __init__(self, points, dimensions, dimension_splits, dimension_size=100):
        super().__init__(points)
        self.buckets = [Bucket(i) for i, _ in enumerate(range(dimension_splits ** dimensions))]
        bucket_size = int(dimension_size / dimension_splits)
        for cl in self.clusters:
            p = self.clusters[cl].points[0]
            point_bucket_coords = [int(c / bucket_size) for c in p.coordinates]
            bucket_id = sum([c * (dimension_splits ** i) for i, c in enumerate(point_bucket_coords)])
            self.buckets[bucket_id].set_cluster(self.clusters[cl])
        for bucket in self.buckets:
            bucket.distance_matrix = self.compute_distance_matrix(bucket.clusters)

    def nearest_clusters(self):
        min_distance = math.inf
        min_id1 = None
        min_id2 = None

        for bucket in self.buckets:
            keys = list(bucket.clusters.keys())
            for i, id1 in enumerate(keys):
                for id2 in keys[i + 1:]:
                    distance = bucket.distance_matrix[id1][id2]
                    if distance < min_distance:
                        min_distance = distance
                        min_id1 = id1
                        min_id2 = id2

        if not min_id1:
            self.unify_buckets()
            return self.nearest_clusters()

        return min_id1, min_id2

    def compute_distance_matrix(self, clusters):
        matrix = {}
        keys = list(clusters.keys())
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
        for bucket in self.buckets:
            if id1 in bucket.clusters and id2 in bucket.clusters:
                bucket.clusters.pop(id2)

                dist_c1 = bucket.distance_matrix[id1]
                dist_c2 = bucket.distance_matrix[id2]
                bucket.distance_matrix[id1] = {k: min(v, dist_c2[k]) for k, v in dist_c1.items() if k in dist_c2}

                bucket.distance_matrix.pop(id2)
                for key in bucket.distance_matrix.keys():
                    bucket.distance_matrix[key].pop(id2)
            elif id2 in bucket.clusters:
                bucket.clusters[id1] = bucket.clusters.pop(id2)
                bucket.distance_matrix[id1] = bucket.distance_matrix.pop(id2)

                for key in bucket.distance_matrix.keys():
                    bucket.distance_matrix[key][id1] = bucket.distance_matrix[key].pop(id2)

    def unify_buckets(self):
        bucket = Bucket(0)
        for cl in self.clusters:
            bucket.set_cluster(self.clusters[cl])
        bucket.distance_matrix = self.compute_distance_matrix(self.clusters)
        self.buckets = [bucket]
