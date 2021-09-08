class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time Complexity = O(max(m,n))
# Space Complexity = O(1)
def getIntersectionNode(headA, headB):
    nodeA = headA
    nodeB = headB

    while nodeA is not nodeB:
        nodeA = headB if nodeA is None else nodeA.next
        nodeB = headA if nodeB is None else nodeB.next

    return nodeA