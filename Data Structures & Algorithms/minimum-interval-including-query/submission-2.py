class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        qAndPos = []
        for i, q in enumerate(queries):
            qAndPos.append([q, i])
        
        qAndPos.sort(key = lambda x: x[0])
        intervals.sort(key = lambda x: x[0])

        minHeap = []

        output = [-1 for i in range(len(queries))]
        i = 0
        for q, pos in qAndPos:
            # add valid intervals
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i][0], intervals[i][1]
                heapq.heappush(minHeap, [e-s+1, e])
                i += 1
                
            # pop expired queries
            # since q1 < q2 and end < q1 => end < q2 => no need to consider the interval again going forward
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            # minHeap empty => no valid candidate intervals for current query
            if minHeap:
                output[pos] = minHeap[0][0]

        return output 

            

