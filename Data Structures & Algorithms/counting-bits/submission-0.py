class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        cross = 1
        for i in range(1, n+1):
            if i == cross*2:
                cross = i
            dp[i] = 1+dp[i-cross]

        return dp