class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start: ListNode, end: ListNode) -> None:
            # 反转从 start 到 end 的这段链表（包含 start 和 end）
            prev = None
            curr = start
            stop = end.next  # 保存 end 的下一个节点作为停止标记
            
            while curr != stop:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            # 注意：这里不返回任何值，因为反转后 start 变成尾，end 变成头
        
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        
        while prev_group_tail:
            # 检查剩余节点是否够 k 个
            start = prev_group_tail.next
            end = start
            for _ in range(k - 1):
                if end is None or end.next is None:
                    return dummy.next
                end = end.next
            
            # 保存下一组的头
            next_group_head = end.next
            
            # 反转当前组
            reverse(start, end)
            
            # 将反转后的组接回链表
            prev_group_tail.next = end      # end 现在是新头
            start.next = next_group_head    # start 现在是新尾
            
            # 移动 prev_group_tail 到下一组的前一个节点
            prev_group_tail = start
        
        return dummy.next