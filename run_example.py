import random

import matplotlib.pyplot as plt

from classes.Point import Point
from versions.SingleLinkageClusteringV1 import SingleLinkageClusteringV1
from versions.SingleLinkageClusteringV2 import SingleLinkageClusteringV2
from versions.SingleLinkageClusteringV3 import SingleLinkageClusteringV3
from versions.SingleLinkageClusteringV4 import SingleLinkageClusteringV4

plot_filename = 'V1_Example_20_3.PNG'
n_points = 20
n_clusters = 3
version = 1  # 1, 2, 3 or 4
random.seed(24011994)


def rand():
    return random.uniform(0., 100.)


points = [
    Point('P' + str(i + 1), [rand(), rand()]) for i in range(n_points)
]

slc = None
if version == 1:
    slc = SingleLinkageClusteringV1(points)
elif version == 2:
    slc = SingleLinkageClusteringV2(points)
elif version == 3:
    slc = SingleLinkageClusteringV3(points)
elif version == 4:
    slc = SingleLinkageClusteringV4(points, dimensions=2, dimension_splits=5)
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

fig.savefig('img/' + plot_filename)
fig.show()
