import random

import matplotlib.pyplot as plt

from classes.Point import Point
from versions.SingleLinkageClusteringV1 import SingleLinkageClusteringV1

n_points = 20
n_clusters = 5
random.seed(24011994)


def rand():
    return random.uniform(0., 100.)


points = [
    Point('P' + str(i + 1), [rand(), rand()]) for i in range(n_points)
]

slc = SingleLinkageClusteringV1(points)
clusterings = slc.clustering(k=n_clusters)
for clustering in clusterings:
    print(clustering)
last_clustering = clusterings[-1]

colors = ['r', 'g', 'b', 'c', 'y', 'm', 'b']

fig = plt.figure()
ax = fig.add_subplot(111)

for idx, cluster_id in enumerate(last_clustering.keys()):
    cluster = last_clustering[cluster_id]
    for point in cluster.points:
        point_coordinates = point.coordinates
        color = colors[idx]
        ax.scatter(point_coordinates[0], point_coordinates[1], c=color)

fig.savefig('img/Example.PNG')
fig.show()
