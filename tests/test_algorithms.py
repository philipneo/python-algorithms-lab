from algorithms.dynamic_programming import edit_distance, longest_increasing_subsequence
from algorithms.graphs import dijkstra, topological_sort


def test_dijkstra_shortest_paths():
    edges = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("C", "B", 1),
        ("B", "D", 5),
        ("C", "D", 8),
    ]

    assert dijkstra(edges, "A") == {"A": 0.0, "B": 3.0, "C": 2.0, "D": 8.0}


def test_topological_sort_respects_dependencies():
    order = topological_sort([("plan", "code"), ("code", "test"), ("test", "ship")])

    assert order.index("plan") < order.index("code")
    assert order.index("code") < order.index("test")
    assert order.index("test") < order.index("ship")


def test_longest_increasing_subsequence():
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_edit_distance():
    assert edit_distance("kitten", "sitting") == 3
