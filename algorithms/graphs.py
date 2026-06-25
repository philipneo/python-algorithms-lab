from __future__ import annotations

from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import Hashable, Iterable

Node = Hashable
WeightedEdge = tuple[Node, Node, float]


def dijkstra(edges: Iterable[WeightedEdge], start: Node) -> dict[Node, float]:
    """Return shortest path distances from start for a non-negative weighted graph."""
    graph: dict[Node, list[tuple[Node, float]]] = defaultdict(list)
    distances: dict[Node, float] = {start: 0.0}
    queue: list[tuple[float, Node]] = [(0.0, start)]

    for source, target, weight in edges:
        if weight < 0:
            raise ValueError("Dijkstra requires non-negative edge weights")
        graph[source].append((target, weight))
        distances.setdefault(source, float("inf"))
        distances.setdefault(target, float("inf"))

    distances[start] = 0.0

    while queue:
        distance, node = heappop(queue)
        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heappush(queue, (candidate, neighbor))

    return distances


def topological_sort(edges: Iterable[tuple[Node, Node]]) -> list[Node]:
    """Return a topological ordering for a directed acyclic graph."""
    graph: dict[Node, list[Node]] = defaultdict(list)
    indegree: dict[Node, int] = defaultdict(int)

    for source, target in edges:
        graph[source].append(target)
        indegree.setdefault(source, 0)
        indegree[target] += 1

    queue = deque(node for node, degree in indegree.items() if degree == 0)
    order: list[Node] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(indegree):
        raise ValueError("Graph contains a cycle")

    return order
