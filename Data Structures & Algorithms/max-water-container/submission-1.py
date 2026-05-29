class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        n = len(heights)
        r = n-1
        result = 0
        while l<r:
            height = min(heights[r], heights[l])
            area = height * (r-l)
            result = max(result, area)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return result
# TC = O(n) , SC = O(1)
