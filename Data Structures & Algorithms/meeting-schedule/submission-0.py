"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    
        sorted_intervals = []
        for interval in intervals:
            sorted_intervals.append([interval.start, interval.end])
        
        sorted_intervals.sort(key = lambda x: x[0])

        for i in range(len(sorted_intervals)):
            # if there is overlap => False
            if i-1 >= 0 and sorted_intervals[i][0] < sorted_intervals[i-1][1]:
                return False
        return True
