class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        
        for i in range(n):
            for j in range(i):
#If the previous number is smaller, then nums[i] can extend the increasing subsequence ending at j.
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) 
# TC = O(n^2) outer loop → O(n) # inner loop → O(n)
#SC = O(n)

