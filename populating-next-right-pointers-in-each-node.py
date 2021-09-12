from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

#BFS
# Time Complexity = O(n)
# Space Complexity = O(n/2+1) (because it is a perfectly balanced binary tree)
def connect(root):
    if root:
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                queue.append(node.left)
                queue.append(node.right)
        return root
    return None

#BFS Without Queue
# Time Complexity = O(n)
# Space Complexity = O(1)
def connect(root):
    if not root:
        return None
    node  = root
    next_node = root.left

    while next_node :
        node.left.next = node.right
        if node.next:
            node.right.next = node.next.left
            node = node.next
        else:
            node = next_node
            next_node = node.left
    return root