class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lists = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            lists[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            lists[i] *= postfix
            postfix *= nums[i] 

        return lists


  

        