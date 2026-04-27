class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1:
            return nums[0]
        
        def rob(l,r):
            cur, prev = 0,0
            for i in range(l, r):
                prev, cur = cur, max(nums[i]+prev, cur)
            return cur
        
        return max(rob(0,n-1), rob(1,n))

#TC = O(n-1) + O(n-1) = O(2n) = O(n)
#SC = O(1)