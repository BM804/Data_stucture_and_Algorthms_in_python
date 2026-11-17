"""Return binary-tree values grouped by depth using breadth-first search.

Each queue level contains exactly the nodes at one depth. Enqueuing children
left-to-right preserves the usual level-order traversal.

Time: O(n). Extra space: O(w), where w is the tree's maximum width.
"""

from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    """A binary-tree node containing an integer."""

    value: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def level_order(root: TreeNode | None) -> list[list[int]]:
    """Return one list per depth; an empty tree returns an empty list."""
    if root is None:
        return []

    levels: list[list[int]] = []
    queue = deque([root])

    while queue:
        level: list[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        levels.append(level)

    return levels


if __name__ == "__main__":
    tree = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )
    assert level_order(tree) == [[3], [9, 20], [15, 7]]
    assert level_order(TreeNode(1)) == [[1]]
    assert level_order(None) == []
    print("All Binary Tree Level Order examples passed.")
