# Top Down Memorization
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        def f(n):
            if n in memo:
                return memo[n]
            memo[n] = f(n-2)+f(n-1)
            return memo[n]
        
        return f(n)
#Time : O(n)
#space : O(n)

        