#!/usr/bin/python3

"""You have n number of locked boxes in front
 of you. Each box is numbered sequentially
 from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    function that checks if the value in the list exists.
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for index in range(len(boxes)):
            boxes_checked = k in boxes[index] and k != index
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
