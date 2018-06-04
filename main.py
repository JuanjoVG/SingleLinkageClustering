from Point import Point
from SingleLinkageClustering import SingleLinkageClustering
import matplotlib.pyplot as plt

points = [
    Point('P1', [1.5, 1.5]),
    Point('P2', [2., 1.]),
    Point('P3', [3., 3.]),
    Point('P4', [4., 5.]),
    Point('P5', [5., 3.])
]

slc = SingleLinkageClustering(points)
clusterings = slc.clustering(k=5)

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

fig.show()
