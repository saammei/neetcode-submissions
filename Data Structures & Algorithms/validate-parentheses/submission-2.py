class Solution:
    def isValid(self, s: str) -> bool:
        pair = { "]":"[", ")":"(", "}":"{", }
        stack = []
        for c in s:
            if c in pair:
                if not stack or stack.pop() != pair[c]:
                    return False
            else:
                stack.append(c)
        return not stack


