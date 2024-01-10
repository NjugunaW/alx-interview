#!/usr/bin/python3

"""
This method determines if all boxes can be opened
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes: List of lists representing boxes and their corresponding keys.

    Returns:
        True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    collected_keys = set()
    opened_boxes = [False] * num_boxes
    opened_boxes[0] = True

    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not opened_boxes[key]:
                opened_boxes[key] = True
                collected_keys.add(key)
                stack.append(key)

    return all(opened_boxes)
