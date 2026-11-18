"""Compute shortest distances from one source with Dijkstra's algorithm.

The graph maps each node to (neighbor, non-negative weight) pairs. Unreachable
nodes have distance None. Every node referenced by an edge is included in the
returned mapping, even if it has no outgoing edges.

Time: O((V + E) log V). Extra space: O(V).
"""

from heapq import heappop, heappush
from itertools import count
from typing import Hashable, Mapping, Sequence, TypeVar

Node = TypeVar("Node", bound=Hashable)


def dijkstra_shortest_paths(
    graph: Mapping[Node, Sequence[tuple[Node, int]]], start: Node
) -> dict[Node, int | None]:
    """Return minimum distances; raise KeyError for a missing start node.

    Negative edge weights are rejected because Dijkstra's greedy choice
    requires every edge weight to be non-negative.
    """
    if start not in graph:
        raise KeyError(f"start node {start!r} is not in the graph")

    nodes = dict.fromkeys(graph)
    for edges in graph.values():
        for neighbor, weight in edges:
            if weight < 0:
                raise ValueError("edge weights must be non-negative")
            nodes.setdefault(neighbor, None)

    distances: dict[Node, int | None] = dict.fromkeys(nodes, None)
    distances[start] = 0

    tie_breaker = count()
    queue: list[tuple[int, int, Node]] = [(0, next(tie_breaker), start)]

    while queue:
        distance, _, node = heappop(queue)
        if distance != distances[node]:
            continue

        for neighbor, weight in graph.get(node, ()):
            candidate = distance + weight
            known = distances[neighbor]
            if known is None or candidate < known:
                distances[neighbor] = candidate
                heappush(queue, (candidate, next(tie_breaker), neighbor))

    return distances


if __name__ == "__main__":
    network = {
        "A": [("B", 4), ("C", 1)],
        "B": [("D", 1)],
        "C": [("B", 2), ("D", 5)],
        "D": [],
        "Z": [],
    }
    assert dijkstra_shortest_paths(network, "A") == {
        "A": 0, "B": 3, "C": 1, "D": 4, "Z": None
    }
    assert dijkstra_shortest_paths({"A": [("B", 0)], "B": []}, "A") == {
        "A": 0, "B": 0
    }

    try:
        dijkstra_shortest_paths({"A": [("B", -1)], "B": []}, "A")
    except ValueError:
        pass
    else:
        raise AssertionError("negative edge should raise ValueError")

    print("All Dijkstra Shortest Paths examples passed.")
