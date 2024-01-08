import unittest

from src.algorithms.dynamic_programming.multistage_graphs import GraphShortestPath
from src.data_structure.graphs.weighted_graph import WeightedGraphFactory


class TestGraphShortestPath(unittest.TestCase):
    def setUp(self):
        self.edges_list = [
            (0, 1, 1),
            (0, 2, 2),
            (0, 3, 5),
            (1, 4, 4),
            (1, 5, 11),
            (2, 4, 9),
            (2, 5, 5),
            (2, 6, 16),
            (3, 6, 2),
            (4, 7, 18),
            (5, 7, 13),
            (6, 7, 2)
        ]
        self.number_of_nodes = 8
        self.graph_object = WeightedGraphFactory(
            number_of_nodes=8,
            edges_list=self.edges_list,
            representation="matrix"
        ).get_graph()

    def test_shortest_path_and_cost(self):
        graph_shortest_path = GraphShortestPath(self.graph_object, self.number_of_nodes, 4)
        cost, path = graph_shortest_path.shortest_path_and_cost()
        assert cost == 9
        assert path == [0, 3, 6, 7]