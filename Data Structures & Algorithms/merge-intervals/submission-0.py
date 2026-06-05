class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort(key= lambda interval: interval[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            start, end = interval[0], interval[1]
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(interval)
        return res