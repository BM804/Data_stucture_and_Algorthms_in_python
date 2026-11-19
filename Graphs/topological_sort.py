"""Order a directed acyclic graph so every edge points forward.

Kahn's algorithm repeatedly removes a node with zero incoming edges. If any
nodes remain, they belong to or depend on a directed cycle and no topological
ordering exists.

Time: O(V + E). Extra space: O(V).
"""

from collections import deque
from typing import Hashable, Mapping, Sequence, TypeVar

Node = TypeVar("Node", bound=Hashable)


def topological_sort(
    graph: Mapping[Node, Sequence[Node]],
) -> list[Node] | None:
    """Return a valid topological order, or None if the graph has a cycle."""
    nodes = dict.fromkeys(graph)
    for neighbors in graph.values():
        for neighbor in neighbors:
            nodes.setdefault(neighbor, None)

    indegree = dict.fromkeys(nodes, 0)
    for node in nodes:
        for neighbor in graph.get(node, ()):
            indegree[neighbor] += 1

    ready = deque(node for node in nodes if indegree[node] == 0)
    order: list[Node] = []

    while ready:
        node = ready.popleft()
        order.append(node)
        for neighbor in graph.get(node, ()):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                ready.append(neighbor)

    return order if len(order) == len(nodes) else None


if __name__ == "__main__":
    graph = {
        "A": ["C"],
        "B": ["C"],
        "C": ["D"],
        "D": [],
        "E": ["D"],
        "F": [],
    }
    order = topological_sort(graph)
    assert order is not None
    position = {node: index for index, node in enumerate(order)}
    assert all(position[source] < position[target]
               for source, neighbors in graph.items()
               for target in neighbors)
    assert topological_sort({"A": ["B"], "B": ["A"]}) is None
    assert topological_sort({"A": ["A"]}) is None
    assert topological_sort({}) == []
    print("All Topological Sort examples passed.")
