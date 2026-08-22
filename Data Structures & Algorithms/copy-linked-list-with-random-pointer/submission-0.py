"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        node_map = dict()
        node = head
        while node:
            node_map[node] = Node(node.val)
            node = node.next

        for old_A in node_map:
            new_A = node_map[old_A]
            new_A.next = node_map[old_A.next] if old_A.next else None
            new_A.random = node_map[old_A.random] if old_A.random else None
        return node_map[head]
