class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            buy = min(prices[i] , buy)
            profit = max(profit, prices[i] - buy)
        return profit

        # TC = O(n), SC= O(1)