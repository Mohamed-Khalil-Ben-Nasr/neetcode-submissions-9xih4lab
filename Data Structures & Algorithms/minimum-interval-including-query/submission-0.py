class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # O(n logn)
        intervals.sort(key = lambda x: x[0])
        
        # O(n ** 2)
        res = [float("inf") for i in range(len(queries))]
        for i, query in enumerate(queries):
            for start, end in intervals:
                if start <= query <= end:
                    res[i] = min(res[i], end - start + 1)
            if res[i] == float("inf"):
                res[i] = -1
        return res
