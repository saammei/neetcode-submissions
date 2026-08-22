class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x in "+-*/":
                a = stack.pop()
                if x == '+':
                    stack[-1] += a
                elif x == '-':
                    stack[-1] -= a
                elif x == '*':
                    stack[-1] *= a
                elif x == '/':
                    stack[-1] = int(stack[-1] / a)
            else:
                stack.append(int(x))
        return stack[-1]

