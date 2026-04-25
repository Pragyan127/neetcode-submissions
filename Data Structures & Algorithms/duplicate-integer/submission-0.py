class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        khoj = {}
        for i, num in enumerate(nums):
            if num in khoj:
                return True
            khoj[num] = i
        return False