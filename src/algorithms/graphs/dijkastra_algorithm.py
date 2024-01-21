import sys
import heapq

"""
    Dijkastra's Algorithm
    Is it being used widely to find the shortest path distance from given source vertex
    in positively weighted graph having all edges.
    * Implementation
        - in Adjacency Matrix Graph : DijkastraShortestPathAdjacencyMatrix
        - in Adjacency List Graph : DijkastraShortestPathAdjacencyList
"""


class DijkastraShortestPathAdjacencyMatrix:
    def __init__(self, graph, number_of_node, source):
        self.graph = graph
        self.number_of_node = number_of_node
        self.distance = [sys.maxsize]*self.number_of_node
        self.parent_node = [0]*self.number_of_node
        self.visited_nodes = [False]*self.number_of_node
        self.distance[source] = 0
        self.source = source

    def __min_distance(self):
        _min, min_index = sys.maxsize, -1

        for node in range(self.number_of_node):
            if self.distance[node] < _min and not self.visited_nodes[node]:
                _min = self.distance[node]
                min_index = node

        return min_index

    def __get_all_shortest_path(self, vertex):
        shortest_paths_from_source = []
        for current_parent in self.parent_node[1:]:
            path = [vertex]

            while current_parent != self.source:
                path = [current_parent] + path
                current_parent = self.parent_node[current_parent]

            path = [self.source] + path
            vertex += 1

            shortest_paths_from_source.append(path)
        return shortest_paths_from_source

    def __find_shortest_paths_and_cost(self):
        for source in range(self.number_of_node):

            start_vertex = self.__min_distance()
            self.visited_nodes[start_vertex] = True

            for neighbour_vertex in range(self.number_of_node):

                if (
                        self.graph[start_vertex][neighbour_vertex] and
                        not self.visited_nodes[neighbour_vertex] and
                        self.distance[neighbour_vertex] > self.distance[start_vertex] + self.graph[start_vertex][neighbour_vertex]
                ):
                    self.distance[neighbour_vertex] = self.distance[start_vertex] + self.graph[start_vertex][neighbour_vertex]
                    self.parent_node[neighbour_vertex] = start_vertex

        shortest_paths_from_source = self.__get_all_shortest_path(1)

        return self.distance, shortest_paths_from_source

    def calculate(self):
        return self.__find_shortest_paths_and_cost()


class DijkastraShortestPathAdjacencyList:
    def __init__(self, graph, number_of_node, source):
        self.graph = graph
        self.number_of_node = number_of_node
        self.distance = [sys.maxsize]*self.number_of_node
        self.parent_node = [0]*self.number_of_node
        self.visited_nodes = [False]*self.number_of_node
        self.distance[source] = 0
        self.source = source
        self.priority_queue = []
        heapq.heappush(self.priority_queue, (0, self.source))

    def __get_all_shortest_path(self, vertex):
        shortest_paths_from_source = []
        for current_parent in self.parent_node[1:]:
            path = [vertex]

            while current_parent != self.source:
                path = [current_parent] + path
                current_parent = self.parent_node[current_parent]

            path = [self.source] + path
            vertex += 1

            shortest_paths_from_source.append(path)
        return shortest_paths_from_source

    def __find_shortest_paths_and_cost(self):
        while self.priority_queue:
            distance, start_vertex = heapq.heappop(self.priority_queue)

            for neighbour_vertex, weight in self.graph[start_vertex]:
                if self.distance[neighbour_vertex] > weight + self.distance[start_vertex]:
                    self.distance[neighbour_vertex] = weight + self.distance[start_vertex]
                    self.parent_node[neighbour_vertex] = start_vertex
                    heapq.heappush(self.priority_queue, (self.distance[neighbour_vertex], neighbour_vertex))

        shortest_paths_from_source = self.__get_all_shortest_path(1)

        return self.distance, shortest_paths_from_source

    def calculate(self):
        return self.__find_shortest_paths_and_cost()
