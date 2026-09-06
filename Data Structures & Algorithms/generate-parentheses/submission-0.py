class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        current = []

        def dfs(left, right):
            if right == n:
                res.append(''.join(current))
                return
            if left < n:
                current.append('(')
                dfs(left + 1, right)
                current.pop()
            if left > right:
                current.append(")")
                dfs(left, right + 1)
                current.pop()

        dfs(0, 0)
        return res
