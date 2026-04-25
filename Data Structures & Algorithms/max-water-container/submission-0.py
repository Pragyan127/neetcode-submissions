class Solution:
    def maxArea(self, h: List[int]) -> int:
        high = 0
        for i in range(len(h)):
            for j in range(i+1, len(h)):
                water = min(h[i], h[j]) * (j-i)
                high = max(water , high)
                
        return high


