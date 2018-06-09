import unittest

from Cluster import Cluster
from Point import Point
from SingleLinkageClustering import SingleLinkageClustering


class SingleLinkageClusteringTest(unittest.TestCase):
    points = {
        'P1': Point('P1', [1.5, 1.5]),
        'P2': Point('P2', [2., 1.]),
        'P3': Point('P3', [3., 3.]),
        'P4': Point('P4', [4., 5.]),
        'P5': Point('P5', [5., 3.])
    }

    correct_clusterings = [
        {'C1': Cluster('C1', [points['P1']]), 'C2': Cluster('C2', [points['P2']]), 'C3': Cluster('C3', [points['P3']]),
         'C4': Cluster('C4', [points['P4']]), 'C5': Cluster('C5', [points['P5']])},
        {'C1': Cluster('C1', [points['P1'], points['P2']]), 'C3': Cluster('C3', [points['P3']]),
         'C4': Cluster('C4', [points['P4']]), 'C5': Cluster('C5', [points['P5']])},
        {'C1': Cluster('C1', [points['P1'], points['P2']]), 'C3': Cluster('C3', [points['P3'], points['P5']]),
         'C4': Cluster('C4', [points['P4']])},
        {'C1': Cluster('C1', [points['P1'], points['P2'], points['P3'], points['P5']]),
         'C4': Cluster('C4', [points['P4']])},
        {'C1': Cluster('C1', [points['P1'], points['P2'], points['P3'], points['P5'], points['P4']])}
    ]

    def setUp(self):
        pass

    def test_simplest_clustering_version_with_toy_case(self):
        slc = SingleLinkageClustering(self.points.values())
        clusterings = slc.clustering(k=1)
        self.assertEqual(clusterings, self.correct_clusterings)


if __name__ == '__main__':
    unittest.main()
