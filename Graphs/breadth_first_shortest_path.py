"""Find a shortest path in an unweighted graph with breadth-first search.

The graph maps each node to its neighbors. The search records each node's
predecessor when first discovered, then rebuilds the path on reaching the
destination. Nodes absent as keys are treated as having no edges.

Time: O(V + E). Extra space: O(V).
"""
from collections import deque
from typing import Mapping, Sequence, TypeVar

Node = TypeVar("Node")


def breadth_first_shortest_path(
    graph: Mapping[Node, Sequence[Node]], start: Node, target: Node
) -> list[Node] | None:
    """Return a minimum-edge path, or None when target cannot be reached."""
    if start == target:
        return [start]

    queue = deque([start])
    predecessor: dict[Node, Node | None] = {start: None}

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, ()):
            if neighbor in predecessor:
                continue

            predecessor[neighbor] = node
            if neighbor == target:
                path: list[Node] = []
                current: Node | None = target
                while current is not None:
                    path.append(current)
                    current = predecessor[current]
                path.reverse()
                return path
            queue.append(neighbor)

    return None


if __name__ == "__main__":
    network = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D", "E"],
        "D": ["B", "C", "F"],
        "E": ["C"],
        "F": [],
        "X": [],
    }
    shortest = breadth_first_shortest_path(network, "A", "F")
    # There are two shortest paths; BFS should return either one.
    assert shortest in (["A", "B", "D", "F"], ["A", "C", "D", "F"])
    assert breadth_first_shortest_path(network, "A", "A") == ["A"]
    assert breadth_first_shortest_path(network, "A", "X") is None
    assert breadth_first_shortest_path({"A": ["B"]}, "A", "B") == ["A", "B"]
    print("All Breadth-First Shortest Path examples passed.")
