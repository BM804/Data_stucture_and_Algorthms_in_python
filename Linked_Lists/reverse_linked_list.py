"""Reverse a singly linked list in place using three pointers.

The previous, current, and next references let each link be redirected
without losing access to the rest of the list.

Time: O(n). Extra space: O(1).
"""

from dataclasses import dataclass


@dataclass
class Node:
    """One integer node in a singly linked list."""

    value: int
    next: "Node | None" = None


def reverse_linked_list(head: Node | None) -> Node | None:
    """Reverse the links and return the new head."""
    previous = None
    current = head

    while current is not None:
        following = current.next
        current.next = previous
        previous = current
        current = following

    return previous


def list_from_values(values: list[int]) -> Node | None:
    """Build a linked list for the runnable examples."""
    head = tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def values_from_list(head: Node | None) -> list[int]:
    """Collect list values; the bounded loop also exposes accidental cycles."""
    values = []
    while head is not None:
        values.append(head.value)
        head = head.next
        if len(values) > 1000:
            raise ValueError("linked list contains a cycle")
    return values


if __name__ == "__main__":
    assert values_from_list(reverse_linked_list(list_from_values([1, 2, 3]))) == [3, 2, 1]
    assert values_from_list(reverse_linked_list(list_from_values([7]))) == [7]
    assert reverse_linked_list(None) is None
    print("All Reverse Linked List examples passed.")
