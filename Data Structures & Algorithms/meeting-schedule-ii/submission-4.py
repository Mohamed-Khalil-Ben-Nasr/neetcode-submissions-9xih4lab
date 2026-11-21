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

        intervals.sort(key = lambda interval : interval.start)
        minHeap = []
        heapq.heappush(minHeap, intervals[0].end)
        for interval in intervals[1:]:
            # if current start >= smallest end => no need for new classroom => remove the smallest end and push the new end 
            # => no overlap
            if minHeap and (minHeap[0] <= interval.start):
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)

        return len(minHeap)

