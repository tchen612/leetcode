# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        q = deque([root])
        result = []
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            result.append(str(node.val) if node else "x")
        return ",".join([str(x) for x in result])
            

    def deserialize(self, data):
        if not data: 
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        index = 1
        while q:
            node = q.popleft()
            if nodes[index] is not "x":
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1
        
            if nodes[index] is not "x":
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root