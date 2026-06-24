"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        ints = []
        for interval in intervals:
            ints.append([interval.start, interval.end])
        ints.sort(key= lambda x: x[0])
        # my approach of tracking the end times of the bookings of each classroom
        # can be replaced by a min heap which returns the classroom thats free the earliest
        # in O(nlogn) 
        heap = []
        for start, end in ints:
            if heap and heap[0]<= start:
                # can be done in one operation => heapq.heapreplace(heap, end)
                heapq.heappop(heap)
                heapq.heappush(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)
