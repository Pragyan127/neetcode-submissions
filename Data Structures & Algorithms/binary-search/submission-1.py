class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] - target == 0:
                return mid
            elif nums[mid] - target > 0:
                r = mid - 1
            else:
                l = mid + 1
        return -1
# TC = O(logn), SC = O(1)