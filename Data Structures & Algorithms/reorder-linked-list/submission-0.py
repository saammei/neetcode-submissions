# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next
        n //= 2
        tmp = head
        for i in range(n - 1):
            tmp = tmp.next
        tmp.next, tmp = None, tmp.next

        prev = None
        while tmp:
            tmp.next, prev, tmp = prev, tmp, tmp.next

        left, right = head, prev
        dummy = ListNode()
        tmp = dummy
        while left and right:
            tmp.next, left = left, left.next
            tmp = tmp.next
            tmp.next, right = right, right.next
            tmp = tmp.next

        tmp.next = left or right

        head = dummy.next

