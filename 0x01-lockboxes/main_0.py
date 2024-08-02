#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

canUnlockAll = __import__('0-lockboxes').canUnlockAll

# Test case 1: All boxes can be unlocked sequentially
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 2: Some boxes contain keys that are out of range
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3]]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 3: Not all boxes can be unlocked
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False

# Test case 4: Only the first box is present
boxes = [[]]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 5: All boxes are empty
boxes = [[], [], [], []]
print(canUnlockAll(boxes))  # Expected output: False

# Test case 6: All boxes can be unlocked with multiple keys
boxes = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 1, 2]]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 7: Large number of boxes with a complex key structure
boxes = [[1, 3, 5], [2, 4], [0, 6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [50], [
    51], [52], [53], [54], [55], [56], [57], [58], [59], [60], [61], [62], [63], [64], [65], [66], [67], [68], [69], [70], [71], [72], [73], [74], [75], [76], [77], [78], [79], [80], [81], [82], [83], [84], [85], [86], [87], [88], [89], [90], [91], [92], [93], [94], [95], [96], [97], [98], [99], []]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 8: Boxes with duplicate keys
boxes = [[1, 1, 1], [2, 2, 2], [3, 3, 3], []]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 9: Boxes with no keys at all
boxes = [[], [], [], []]
print(canUnlockAll(boxes))  # Expected output: False

# Test case 10: Boxes with circular dependencies
boxes = [[1], [2], [0]]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 11
boxes = [[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], [
    7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7], [4, 2, 9, 6, 6, 5, 5], ]
print(canUnlockAll(boxes))  # Expected output: False

# Test case 12
boxes = [[10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [], [
    6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6]]
print(canUnlockAll(boxes))  # Expected output: True
