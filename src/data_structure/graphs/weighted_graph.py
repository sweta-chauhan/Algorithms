class GraphRepresentation:
    adjacent_weighted_matrix = "matrix"
    adjacent_weighted_list = "list"


class AdjacentWeightedMatrix:
    def __init__(self, number_of_edges, edges_list):
        self.edges_list = edges_list
        self.graph = [[0 for _ in range(number_of_edges)] for _ in range(number_of_edges)]

    def get_graph(self):
        for edge_start_vertex, edge_end_vertex, weight in self.edges_list:
            self.graph[edge_start_vertex][edge_end_vertex] = weight
        return self.graph


class AdjacentWeightedList:
    def __init__(self, number_of_edges, edges_list):
        self.edges_list = edges_list
        self.graph = [[] for _ in range(number_of_edges)]

    def get_graph(self):
        for edge_start_vertex, edge_end_vertex, weight in self.edges_list:
            self.graph[edge_start_vertex] = (edge_end_vertex, weight)
        return self.graph


class WeightedGraphFactory:
    def __init__(self, number_of_nodes, edges_list, representation):
        self.number_of_nodes = number_of_nodes
        self.edges_list = edges_list
        self.representation = representation

    def get_graph(self):
        if self.representation == GraphRepresentation.adjacent_weighted_list:
            return AdjacentWeightedList(self.number_of_nodes, self.edges_list).get_graph()
        elif self.representation == GraphRepresentation.adjacent_weighted_matrix:
            return AdjacentWeightedMatrix(self.number_of_nodes, self.edges_list).get_graph()
