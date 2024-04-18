#!/usr/bin/python3

"""
Lockboxes Problem:

Given a list of lockboxes represented by 'boxes', determine
if all the boxes can be unlocked. Each box contains keys to
other boxes, where a key with the same number as a box opens
that box. The first box boxes[0] is unlocked.

Function Description:

def can_unlock_all(boxes):
    Determines whether all boxes can be opened based on the
    keys found in the boxes.

Args:
    boxes (List[List[int]]): A list of lockboxes represented
    by lists, where each inner list contains the keys to other boxes.

Returns:
    bool: True if all boxes can be opened, False otherwise.
"""


def can_unlock_all(boxes):
    if not boxes:
        return False

    num_boxes = len(boxes)
    visited = set()
    queue = [0]  # Start with the first box
    visited.add(0)

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < num_boxes and key not in visited:
                queue.append(key)
                visited.add(key)

    return len(visited) == num_boxes
