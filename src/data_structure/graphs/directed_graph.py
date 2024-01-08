from collections import defaultdict


class GraphRepresentation:
    adjacent_weighted_matrix = "matrix"
    adjacent_weighted_list = "list"


class AdjacentDirectedMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edges(self, start_vertex, end_vertex):
        self.graph[start_vertex][end_vertex] = 1

    def get_graph(self):
        return self.graph


class AdjacentDirectedList:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edges(self, start_vertex, end_vertex):
        self.graph[start_vertex].append(end_vertex)

    def get_graph(self):
        return self.graph


class DirectedGraphFactory:
    def __init__(self, number_of_nodes, edges_list, representation):
        self.number_of_nodes = number_of_nodes
        self.edges_list = edges_list
        self.representation = representation

    def get_graph(self):
        if self.representation == GraphRepresentation.adjacent_weighted_list:
            graph = AdjacentDirectedList(self.number_of_nodes)

            for edge_start_vertex, edge_end_vertex in self.edges_list:
                graph.add_edges(edge_start_vertex, edge_end_vertex)

            return graph.get_graph()

        elif self.representation == GraphRepresentation.adjacent_weighted_matrix:
            graph = AdjacentDirectedMatrix(self.number_of_nodes)
            for edge_start_vertex, edge_end_vertex in self.edges_list:
                graph.add_edges(edge_start_vertex, edge_end_vertex)

            return graph.get_graph()