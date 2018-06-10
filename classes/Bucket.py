class Bucket:
    def __init__(self, id):
        self.id = id
        self.clusters = {}
        self.distance_matrix = {}

    def set_cluster(self, cluster):
        self.clusters[cluster.id] = cluster
