import unittest

from src.algorithms.graphs.dijkastra_algorithm import DijkastraShortestPathAdjacencyMatrix, \
    DijkastraShortestPathAdjacencyList
from src.data_structure.graphs.weighted_graph import WeightedGraphFactory


class TestDijkastraShortestPathAdjacencyMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.edges_list = [
            (0, 1, 4),
            (0, 7, 8),
            (1, 0, 4),
            (1, 2, 8),
            (1, 7, 11),
            (2, 1, 8),
            (2, 3, 7),
            (2, 5, 4),
            (2, 8, 2),
            (3, 2, 7),
            (3, 4, 9),
            (3, 5, 14),
            (4, 3, 9),
            (4, 5, 10),
            (5, 4, 10),
            (5, 2, 4),
            (5, 3, 14),
            (5, 6, 2),
            (6, 5, 2),
            (6, 7, 1),
            (6, 8, 6),
            (7, 0, 8),
            (7, 1, 11),
            (7, 6, 1),
            (7, 8, 7),
            (8, 2, 2),
            (8, 6, 6),
            (8, 7, 7),

        ]
        self.number_of_nodes = 9
        self.graph_object = WeightedGraphFactory(
            number_of_nodes=self.number_of_nodes,
            edges_list=self.edges_list,
            representation="matrix"
        ).get_graph()

    def test_dijkastra_algorithm(self):
        graph_shortest_path = DijkastraShortestPathAdjacencyMatrix(self.graph_object, self.number_of_nodes, 0)
        cost, shortest_paths_from_source = graph_shortest_path.calculate()
        assert cost == [0, 4, 12, 19, 21, 11, 9, 8, 14]
        assert shortest_paths_from_source == [
            [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 7, 6, 5, 4], [0, 7, 6, 5], [0, 7, 6], [0, 7], [0, 1, 2, 8]
        ]



class TestDijkastraShortestPathAdjacencyList(unittest.TestCase):
    def setUp(self) -> None:
        self.edges_list = [
            (0, 1, 4),
            (0, 7, 8),
            (1, 0, 4),
            (1, 2, 8),
            (1, 7, 11),
            (2, 1, 8),
            (2, 3, 7),
            (2, 5, 4),
            (2, 8, 2),
            (3, 2, 7),
            (3, 4, 9),
            (3, 5, 14),
            (4, 3, 9),
            (4, 5, 10),
            (5, 4, 10),
            (5, 2, 4),
            (5, 3, 14),
            (5, 6, 2),
            (6, 5, 2),
            (6, 7, 1),
            (6, 8, 6),
            (7, 0, 8),
            (7, 1, 11),
            (7, 6, 1),
            (7, 8, 7),
            (8, 2, 2),
            (8, 6, 6),
            (8, 7, 7),

        ]
        self.number_of_nodes = 9
        self.graph_object = WeightedGraphFactory(
            number_of_nodes=self.number_of_nodes,
            edges_list=self.edges_list,
            representation="list"
        ).get_graph()

    def test_dijkastra_algorithm(self):
        graph_shortest_path = DijkastraShortestPathAdjacencyList(self.graph_object, self.number_of_nodes, 0)
        cost, shortest_paths_from_source = graph_shortest_path.calculate()
        assert cost == [0, 4, 12, 19, 21, 11, 9, 8, 14]
        assert shortest_paths_from_source == [
             [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 7, 6, 5, 4], [0, 7, 6, 5], [0, 7, 6], [0, 7], [0, 1, 2, 8]
         ]