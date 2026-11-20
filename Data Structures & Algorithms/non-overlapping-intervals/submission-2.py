class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(n logn)
        # basically greedy approach
        # minimize future overlaps by always deleting the interval with the larger end
        intervals.sort(key = lambda interval : interval[0])
        res = 0 
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # no overlap
            if prevEnd <= start:
                prevEnd = end
            # overlap
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        
        return res