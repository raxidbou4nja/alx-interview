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

def canUnlockAll(boxes):
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    num_boxes = len(boxes)
    
    for key in range(1, num_boxes):
        box_checked = False
        for idx, box in enumerate(boxes):
            if key in box and idx != key:
                box_checked = True
                break
        if not box_checked:
            return False
    return True
