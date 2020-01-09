from collections import defaultdict
import heapq


def read_input(filename):
    with open(filename, "rt") as input_file:
        return [
            list(map(str.strip, line.split(')')))
            for line in input_file
        ]


def build_graph(edges, undirected=False):
    graph = defaultdict(list)

    for start, end in edges:
        graph[start].append(end)
        if undirected:
            graph[end].append(start)

    return graph


def count_orbits(directed_graph):

    def visit_node(node, depth):
        oribit_count = depth
        for neighbour_node in directed_graph[node]:
            oribit_count += visit_node(neighbour_node, depth + 1)
        return oribit_count

    return visit_node('COM', 0)


def find_shortest_path_distance(graph, start_node, end_node):
    # Performs a simple breadth first search to find the shortest path between two nodes
    visited_nodes = set()

    frontier = []
    heapq.heappush(frontier, (0, start_node))

    while frontier:
        distance, current_node = heapq.heappop(frontier)
        visited_nodes.add(current_node)

        if current_node == end_node:
            return distance

        for adjacent_node in graph[current_node]:
            if adjacent_node not in visited_nodes:
                heapq.heappush(frontier, (distance + 1, adjacent_node))


def main():
    filename = "input.txt"
    orbit_edges = read_input(filename)
    directed_graph = build_graph(orbit_edges)

    total_orbit_count = count_orbits(directed_graph)
    print(f'Part 1: {total_orbit_count}')

    undirected_graph = build_graph(orbit_edges, undirected=True)
    shortest_path_distance = find_shortest_path_distance(
        graph=undirected_graph,
        start_node='YOU',
        end_node='SAN',
    )
    num_orbit_hops = shortest_path_distance - 2
    print(f'Part 2: {num_orbit_hops}')


if __name__ == "__main__":
    main()
