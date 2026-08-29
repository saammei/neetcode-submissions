# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        result = 0

        def dfs(node):
            nonlocal count
            nonlocal result

            if not node or count >= k:
                return

            dfs(node.left)

            count += 1
            if count == k:
                result = node.val
                return

            dfs(node.right)

        dfs(root)
        return result
