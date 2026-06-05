from math import floor, ceil
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for i in tokens:
            if i in "*+-/":
                a,b = stk.pop(), stk.pop()

                if i == '*':
                    stk.append(b*a)
                elif i == '+':
                    stk.append(b+a)
                elif i == '-':
                    stk.append(b-a)
                else:
                    div = b/a
                    if div < 0:
                        stk.append(ceil(div))
                    else:
                        stk.append(floor(div))
            else:
                stk.append(int(i))
        return stk[0]

# TC = O(n), SC = O(n)