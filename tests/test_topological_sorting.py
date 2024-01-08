import unittest

from src.algorithms.graphs.topoligical_sorting import GraphTopologicalSorting
from src.data_structure.graphs.directed_graph import DirectedGraphFactory


class TestGraphShortestPath(unittest.TestCase):
    def setUp(self):
        self.edges_list = [
            (5, 2),
            (5, 0),
            (4, 0),
            (4, 1),
            (2, 3),
            (3, 1),
        ]
        self.number_of_nodes = 6
        self.graph_object = DirectedGraphFactory(
            number_of_nodes=self.number_of_nodes,
            edges_list=self.edges_list,
            representation="list"
        ).get_graph()

    def test_shortest_path_and_cost(self):
        graph = GraphTopologicalSorting(self.graph_object, self.number_of_nodes)
        sorted_ordered_vertex_list = graph._sort()
        assert sorted_ordered_vertex_list == [5, 4, 3, 2, 1, 0]
