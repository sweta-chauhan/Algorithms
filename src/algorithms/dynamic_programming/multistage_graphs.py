"""
Multistage Graphs :- Directed, weighted graph in which nodes can be divided in stages.
"""
from math import inf


class GraphShortestPath:
    def __init__(self, graph, number_of_node, stages):
        self.graph = graph
        self.number_of_node = number_of_node
        self.stages = stages

    def shortest_path_and_cost(self):
        cost_data = [0 for _ in range(self.number_of_node)]
        destination_vertex = [0 for _ in range(self.number_of_node)]
        path = [0 for _ in range(self.stages)]

        cost_data[-1] = 0
        destination_vertex[-1] = self.number_of_node-1

        for possible_vertex in range(self.number_of_node-2, -1, -1):
            local_minimum_possible_cost = inf

            for neighbour_vertex in range(possible_vertex, self.number_of_node):
                cost = self.graph[possible_vertex][neighbour_vertex] + cost_data[neighbour_vertex]

                if self.graph[possible_vertex][neighbour_vertex] != 0 and cost < local_minimum_possible_cost:
                    local_minimum_possible_cost = cost
                    destination_vertex[possible_vertex] = neighbour_vertex

            cost_data[possible_vertex] = local_minimum_possible_cost
        path[0] = 0

        for stage in range(1, self.stages):
            path[stage] = destination_vertex[path[stage-1]]
        return cost_data[0], path, destination_vertex






