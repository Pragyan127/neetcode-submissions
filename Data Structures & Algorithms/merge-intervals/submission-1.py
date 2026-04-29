class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])   

        merge = []

        for i in range(len(intervals)):
            if not merge or merge[-1][1] < intervals[i][0]:
                merge.append(intervals[i]) 
            
            else:
                merge[-1] = [merge[-1][0], max(merge[-1][1], intervals[i][1])]
        return merge
        