class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)

        for point in points:
            x, y = point
            distance = math.sqrt((x - 0)**2 + (y - 0)**2)
            heapq.heappush(minHeap, (distance, [x,y]))
        
        res = []
        while k > 0:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1
        
        return res
