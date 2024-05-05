#!/usr/bin/python3


def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    n = len(boxes)
    visited = set()
    visited.add(0)
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n
