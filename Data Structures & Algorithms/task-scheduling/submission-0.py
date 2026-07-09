from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        cyclesCount = 0
        while maxHeap or q:
            cyclesCount += 1
            if maxHeap:
                maxFreq = heapq.heappop(maxHeap) + 1
                if maxFreq < 0:
                    q.append([maxFreq, cyclesCount + n])
            if q and q[0][1] == cyclesCount:
                heapq.heappush(maxHeap, q.popleft()[0])
        return cyclesCount
        