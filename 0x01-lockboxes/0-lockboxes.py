def canUnlockAll(boxes):

    int n = boxes.list()

    unlocked_boxes = recursive_unlock(boxes, n)
    for box in unlocked_boxes:
        if -1 not in box:
            return false
    
    return true



def recursive_unlock(boxes, n):

    int i = 0
    int j = 0

    if (boxes[i].empty()) is true:
        
        return boxes

    for i in range of (n):
        for j in range (boxes[i].length):
            if boxes[i][j] == -1:
                pass
            else:
                boxes[boxes[[i, j]]].append(-1)
                recursive_unlock(boxes, n):
                
