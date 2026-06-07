class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        n = len(heights)

        for i, height in enumerate(heights):
            start = i
            while stk and stk[-1][0] > height:
                h, j = stk.pop()
                w = i-j
                max_area = max(max_area, w*h)
                start = j
            
            stk.append((height, start))

        while stk:
            h,j = stk.pop()
            w = n-j
            a = w * h
            max_area = max(max_area, a)
        
        return max_area

#TC = SC = O(n)