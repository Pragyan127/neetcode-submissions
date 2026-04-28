class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxv, minv = nums[0], nums[0]
    
        res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                maxv, minv = minv,maxv
            
            maxv = max(nums[i], maxv*nums[i])
            minv = min(nums[i], minv * nums[i])
            res = max(res, maxv)
        
        return res
