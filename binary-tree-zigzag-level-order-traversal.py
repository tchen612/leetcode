from collections import deque 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Time Complexity = O(n)
# Space Complexity = O(n)
def zigzagLevelOrder(root):
    if not root:
        return []

    queue = deque()
    queue.append(root)
    result = []
    direction = 1
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)

        result.append(level[::direction])
        direction *= -1

    return result