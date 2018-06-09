import random
import time

from Point import Point
from SingleLinkageClustering import SingleLinkageClustering

## Time tests

test_sizes = [10, 100]
replications = 5


def rand():
    return random.uniform(0., 100.)


def generate_points(n):
    return [Point('P' + str(id + 1), [rand(), rand()]) for id in range(n)]


results = {}

random.seed(24011994)
for test_size in test_sizes:
    for replication in range(replications):
        print('Executing..', test_size, replication)
        points = generate_points(test_size)

        start_time = time.time()
        slc = SingleLinkageClustering(points)
        slc.clustering(k=1)
        total_time = time.time() - start_time

        if test_size not in results:
            results[test_size] = {}
        results[test_size][replication] = total_time

print(results)

## Simple clustering example with plot

# points = [
#     Point('P1', [1.5, 1.5]),
#     Point('P2', [2., 1.]),
#     Point('P3', [3., 3.]),
#     Point('P4', [4., 5.]),
#     Point('P5', [5., 3.])
# ]
# slc = SingleLinkageClustering(points)
# slc.clustering(k=1)
# for clustering in clusterings:
#     print(clustering)
# last_clustering = clusterings[-1]
#
# colors = ['r', 'g', 'b', 'c', 'y', 'm', 'b']
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
#
# for idx, cluster_id in enumerate(last_clustering.keys()):
#     cluster = last_clustering[cluster_id]
#     for point in cluster.points:
#         point_coordinates = point.coordinates
#         color = colors[idx]
#         ax.scatter(point_coordinates[0], point_coordinates[1], c=color)
#
# fig.show()
