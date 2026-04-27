class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n==2:
            return max(nums[0], nums[1])

        cur1, prev1 = max(nums[0], nums[1]), nums[0]
        cur2, prev2 = max(nums[1], nums[2]), nums[1]

        for i in range(3,n):
            prev2, cur2 = cur2, max(nums[i]+ prev2, cur2 )

        for i in range(2,n-1):
            prev1, cur1 = cur1, max(nums[i]+ prev1, cur1 )

        return max(cur1, cur2)