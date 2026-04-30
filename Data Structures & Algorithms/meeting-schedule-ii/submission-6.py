"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        heap = []
        intervals.sort(key = lambda i:i.start)

        heapq.heappush(heap, intervals[0].end)
        maximumRooms = 1
        for i in intervals[1:]:
            while heap and heap[0]<=i.start:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)
            maximumRooms = max(len(heap), maximumRooms)
        return maximumRooms

        # TC = O(nlogn) SC = O(n)