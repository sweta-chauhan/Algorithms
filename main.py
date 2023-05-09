from src.data_structure.graphs.weighted_graph import WeightedGraphFactory
from src.algorithms.dynamic_programming.multistage_graphs import GraphShortestPath


if __name__ == "__main__":
    edges_list = [
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
    number_of_nodes=8
    graph_object = WeightedGraphFactory(number_of_nodes=8, edges_list=edges_list, representation="matrix").get_graph()
    graph_shortest_path = GraphShortestPath(graph_object, number_of_nodes, 4)
    print(graph_shortest_path.shortest_path_and_cost())

