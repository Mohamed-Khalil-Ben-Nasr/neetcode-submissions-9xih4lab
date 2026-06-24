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

        ints = []
        for interval in intervals:
            ints.append([interval.start, interval.end])
        ints.sort(key= lambda x: x[0])
        res = 1
        bookedUntil = []
        bookedUntil.append(ints[0][1])
        for i in range(1, len(intervals)):
            print(ints[i])
            noOverlap = False
            for j in range(len(bookedUntil)):
                # if no overlap
                if bookedUntil[j] <= ints[i][0]:
                    bookedUntil[j] = ints[i][1]
                    noOverlap = True
                    break
            # if we reach here, that means there is an overlap
            # and we cant schedule this meeting in any of the allocated classrooms
            if not noOverlap:
                print("this interval overlapped, ", ints[i])
                res += 1
                bookedUntil.append(ints[i][1])

        return res