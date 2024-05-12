def Dijkstra(Graph, start_node, no_of_vertices):
    nodes = {node: float('inf') for node in range(no_of_vertices)}
    nodes[start_node] = 0
    visited = set()

    while len(visited) < no_of_vertices:
        print(nodes)
        vertex = min((node, distance) for node, distance in nodes.items() if node not in visited)[0]
        visited.add(vertex)

        for edge, cost in Graph.items():
            if vertex in edge:
                other_node = edge[0] if edge[1] == vertex else edge[1]
                new_cost = nodes[vertex] + cost
                if new_cost < nodes[other_node]:
                    nodes[other_node] = new_cost

    return nodes

if __name__ == "__main__":
    graph = {
        (0, 1): 50,
        (0, 2): 45,
        (0, 3): 10,
        (1, 2): 10,
        (1, 3): 15,
        (2, 4): 30,
        (3, 4): 15,
        (4, 1): 20,
        (5, 4): 3,
    }

    start_node = 0
    Dijkstra(graph, start_node, 6)
