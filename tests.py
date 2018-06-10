import unittest

from classes.Cluster import Cluster
from classes.Point import Point
from versions.SingleLinkageClusteringV1 import SingleLinkageClusteringV1
from versions.SingleLinkageClusteringV2 import SingleLinkageClusteringV2
from versions.SingleLinkageClusteringV3 import SingleLinkageClusteringV3
from versions.SingleLinkageClusteringV4 import SingleLinkageClusteringV4


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

    def test_first_clustering_version_with_toy_case(self):
        slc = SingleLinkageClusteringV1(self.points.values())
        clusterings = slc.clustering(k=1)
        self.assertEqual(clusterings, self.correct_clusterings)

    def test_second_clustering_version_with_toy_case(self):
        slc = SingleLinkageClusteringV2(self.points.values())
        clusterings = slc.clustering(k=1)
        self.assertEqual(clusterings, self.correct_clusterings)

    def test_third_clustering_version_with_toy_case(self):
        slc = SingleLinkageClusteringV3(self.points.values())
        clusterings = slc.clustering(k=1)
        self.assertEqual(clusterings, self.correct_clusterings)

    def test_fourth_clustering_version_with_toy_case(self):
        slc = SingleLinkageClusteringV4(self.points.values(), 2, 3, dimension_size=6)
        clusterings = slc.clustering(k=1)
        self.assertEqual(clusterings, self.correct_clusterings)


if __name__ == '__main__':
    unittest.main()
