from day06 import build_graph, count_orbits, find_shortest_path_distance


def test_sample_program_part1():
    orbit_edges = [
        ('COM', 'B'),
        ('B', 'C'),
        ('C', 'D'),
        ('D', 'E'),
        ('E', 'F'),
        ('B', 'G'),
        ('G', 'H'),
        ('D', 'I'),
        ('E', 'J'),
        ('J', 'K'),
        ('K', 'L'),
    ]
    graph = build_graph(orbit_edges)
    assert count_orbits(graph) == 42


def test_sample_program_part2():
    orbit_edges = [
        ('COM', 'B'),
        ('B', 'C'),
        ('C', 'D'),
        ('D', 'E'),
        ('E', 'F'),
        ('B', 'G'),
        ('G', 'H'),
        ('D', 'I'),
        ('E', 'J'),
        ('J', 'K'),
        ('K', 'L'),
        ('K', 'YOU'),
        ('I', 'SAN'),
    ]
    undirected_graph = build_graph(orbit_edges, undirected=True)
    shortest_path_distance = find_shortest_path_distance(
        graph=undirected_graph,
        start_node='YOU',
        end_node='SAN',
    )
    num_orbit_hops = shortest_path_distance - 2
    assert num_orbit_hops == 4
