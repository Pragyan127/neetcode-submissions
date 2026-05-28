class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            high, low = n-1, i+1

            while low<high:
                sums = nums[i]+ nums[low] + nums[high]
                if sums == 0:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while high>low and nums[low] == nums[low-1]:
                        low += 1
                    while high>low and nums[high] == nums[high+1]:
                        high -= 1
                elif sums < 0:
                    low += 1           
                else:
                    high -= 1
        return result