class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Space Complexity = O(max(m,n))
# Time Complexity = O(max(m,n))
def addTwoNumbers(list1, list2):
    dummy = ListNode()
    current = dummy
    carry = 0
    while list1 or list2 or carry:
        val1 = list1.val if list1 else 0
        val2 = list2.val if list2 else 0
        
        sum_result = val1 + val2 + carry  
        value = sum_result % 10
        carry = sum_result // 10
        
        current.next = ListNode(value)
        current = current.next
        
        list1 = list1.next if list1 else None
        list2 = list2.next if list2 else None
    return dummy.next