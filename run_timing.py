import random
import statistics
import time

import matplotlib.pyplot as plt

from classes.Point import Point
from versions.SingleLinkageClusteringV1 import SingleLinkageClusteringV1
from versions.SingleLinkageClusteringV2 import SingleLinkageClusteringV2
from versions.SingleLinkageClusteringV3 import SingleLinkageClusteringV3
from versions.SingleLinkageClusteringV4 import SingleLinkageClusteringV4

test_sizes = [10, 50, 150, 300, 500, 750, 1000]
replications = 5
dimensions = 2


def rand():
    return random.uniform(0., 100.)


def generate_points(n):
    return [Point('P' + str(id + 1), [rand() for _ in range(dimensions)]) for id in range(n)]


results = {}

random.seed(24011994)
for test_size in test_sizes:
    for replication in range(replications):
        print('Executing..', test_size, replication)
        points = generate_points(test_size)

        print('- V1', test_size, replication)
        start_time = time.time()
        slc = SingleLinkageClusteringV1(points)
        slc.clustering(k=1)
        total_time_V1 = time.time() - start_time

        print('- V2', test_size, replication)
        start_time = time.time()
        slc = SingleLinkageClusteringV2(points)
        slc.clustering(k=1)
        total_time_V2 = time.time() - start_time

        print('- V3', test_size, replication)
        start_time = time.time()
        slc = SingleLinkageClusteringV3(points)
        slc.clustering(k=1)
        total_time_V3 = time.time() - start_time

        print('- V4', test_size, replication)
        start_time = time.time()
        slc = SingleLinkageClusteringV4(points, dimensions, 2)
        slc.clustering(k=1)
        total_time_V4 = time.time() - start_time

        if test_size not in results:
            results[test_size] = {}
        results[test_size][replication] = {'V1': total_time_V1, 'V2': total_time_V2, 'V3': total_time_V3,
                                           'V4': total_time_V4}

print(results)

V1_times = [statistics.mean([v['V1'] for v in results[size].values()]) for size in test_sizes]
plt.plot(test_sizes, V1_times, c='r')
V2_times = [statistics.mean([v['V2'] for v in results[size].values()]) for size in test_sizes]
plt.plot(test_sizes, V2_times, c='g')
V3_times = [statistics.mean([v['V3'] for v in results[size].values()]) for size in test_sizes]
plt.plot(test_sizes, V3_times, c='b')
V4_times = [statistics.mean([v['V4'] for v in results[size].values()]) for size in test_sizes]
plt.plot(test_sizes, V4_times, c='y')

plt.legend(['V1', 'V2', 'V3', 'V4'], loc='upper left')

plt.savefig('img/Timing.PNG')
plt.show()
