# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList1(self, head: Optional[ListNode]) -> None:
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

    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        right_head = slow.next
        slow.next = None

        curr, prev = right_head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        left, right = head, prev
        while right:
            next_l, next_r = left.next, right.next

            left.next = right
            right.next = next_l

            left = next_l
            right = next_r

