class GraphTopologicalSorting:
    def __init__(self, graph, number_of_node):
        self.graph = graph
        self.number_of_node = number_of_node
        self.visited_node = [False]*number_of_node
        self.node_in_topological_stack = []

    def _sort(self):
        def depth_first_search(node):
            self.visited_node[node] = True

            for neighbour_node in self.graph[node]:
                if not self.visited_node[node]:
                    depth_first_search(neighbour_node)

            self.node_in_topological_stack.append(node)

        for node in range(self.number_of_node):
            if not self.visited_node[node]:
                depth_first_search(node)

        return self.node_in_topological_stack[::-1]

