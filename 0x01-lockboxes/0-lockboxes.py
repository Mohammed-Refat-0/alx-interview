#!/usr/bin/python3
'''A module of lockboxes algorithm.
'''


def canUnlockAll(boxes):
    """Return True if all boxes (list of lists containing keys for unlocking boxes) 
    can be opened, else return False.
    """
    def recursive_unlock(boxes, unlocked_boxes, box_index):
        for key in boxes[box_index]:
            if key not in unlocked_boxes and 0 <= key < len(boxes):
                unlocked_boxes.add(key)
                recursive_unlock(boxes, unlocked_boxes, key)

    unlocked_boxes = set([0])
    recursive_unlock(boxes, unlocked_boxes, 0)

    return len(unlocked_boxes) == len(boxes)
