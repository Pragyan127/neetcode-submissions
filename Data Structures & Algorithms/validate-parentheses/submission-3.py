class Solution:
    def isValid(self, s: str) -> bool:
        check = {')' : '(', '}':'{', ']':'[' }
        stack = []
        for c in s:
            if c in check:
                if stack and stack[-1] == check[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0