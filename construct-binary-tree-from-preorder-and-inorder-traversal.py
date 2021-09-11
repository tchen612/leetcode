from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity = O(n)
# Space Complexity = O(n)
def buildTree(preorder, inorder):
    preorder = deque(preorder)
    return buildTreeHelper(preorder, inorder)

def buildTreeHelper(preorder, inorder):
    if inorder:
        root_value = preorder.popleft()
        root_index = inorder.index(root_value)
        root = TreeNode(inorder[root_index])
        root.left = buildTreeHelper(preorder, inorder[0:root_index])
        root.right = buildTreeHelper(preorder, inorder[root_index+1:])
        return root