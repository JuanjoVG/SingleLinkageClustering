import copy

from Cluster import Cluster


class SingleLinkageClustering:
    def __init__(self, points):
        self.points = points
        self.clusters = {'C' + str(idx + 1): Cluster('C' + str(idx + 1), [p]) for idx, p in enumerate(self.points)}
        self.clusterings = [copy.deepcopy(self.clusters)]

    def clustering(self, k=1):
        while len(self.clusters.keys()) > k:
            id1, id2 = self.nearest_clusters()
            self.clusterize(id1, id2)
            self.clusterings.append(copy.deepcopy(self.clusters))
        return self.clusterings

    def nearest_clusters(self):
        raise NotImplementedError

    def distance_between_clusters(self, id1, id2):
        c1 = self.clusters[id1]
        c2 = self.clusters[id2]
        return c1.distance(c2)

    def clusterize(self, id1, id2):
        c1 = self.clusters[id1]
        c2 = self.clusters[id2]
        c1.merge(c2)
        self.clusters.pop(id2)
