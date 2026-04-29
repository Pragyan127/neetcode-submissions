class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda i : i[1])

        prev = intervals[0][1]
        for i in range(1, len(intervals)):

            if prev > intervals[i][0]:
                count += 1
            
            else:
                prev = intervals[i][1]
        
        return count
        #TC = O(nlogn), SC = O(1) including sorting O(n)
            
        