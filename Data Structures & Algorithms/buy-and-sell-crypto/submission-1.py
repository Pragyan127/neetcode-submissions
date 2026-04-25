class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        minbuy = prices[0]

        for sell in prices:
            profit = max((sell-minbuy), profit)
            minbuy = min(sell, minbuy)
        return profit
        
        # l,r = 0,1
        # profit = 0

        # while r<len(prices):
        #     if prices[r]>prices[l]:
        #         profit = max((prices[r]-prices[l]), profit)
        #     else:
        #         l=r
        #     r+=1
        
        # return profit

        #Brutal Force

        # prof = 0

        # for i in range(len(prices)-1):
        #     buy = prices[i]
        #     for j in range (i+1, len(prices)):
        #         sell = prices[j]
        #         prof = max((sell-buy), prof)
        # return(prof)
        
            
