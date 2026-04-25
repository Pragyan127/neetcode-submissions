class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = prices[0]
        for i in range(1,len(prices)):
            res = max(prices[i] - l, res)
            l = min(l, prices[i])
        return res
