import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for s in stones:
            heapq.heappush(heap, -s)
        while len(heap) >= 2:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x > y:
                newStone = x - y
                heapq.heappush(heap, -newStone)
        if not heap:
            return 0
        return -heap[0]
            