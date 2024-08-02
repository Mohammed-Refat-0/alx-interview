#!/usr/bin/python3
'''A module of lockboxes algorithm.
'''


def canUnlockAll(boxes):
    """Return True if all boxes (list of lists containing keys for unlocking boxes) 
    can be opened, else return False.
    """
    unlocked_boxes = set([0])
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key not in unlocked_boxes and 0 <= key < len(boxes):
                unlocked_boxes.add(key)
                keys.append(key)

    return len(unlocked_boxes) == len(boxes)
