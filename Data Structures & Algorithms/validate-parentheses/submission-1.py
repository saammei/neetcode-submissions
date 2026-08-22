class Solution:
    def isValid(self, s: str) -> bool:
        pair = { "]":"[", ")":"(", "}":"{", }
        stack = []
        for x in s:
            if x in "[({":
                stack.append(x)
            else:
                if len(stack) == 0 or stack.pop() != pair[x]:
                    return False
        return len(stack) == 0

