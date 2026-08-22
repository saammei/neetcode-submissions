# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        over = 0
        dummy = ListNode()
        node = dummy
        while l1 or l2 or over:
            val = over
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if val >= 10:
                over = 1
                val -= 10
            else:
                over = 0
            node.next = ListNode(val)
            node = node.next
        return dummy.next
