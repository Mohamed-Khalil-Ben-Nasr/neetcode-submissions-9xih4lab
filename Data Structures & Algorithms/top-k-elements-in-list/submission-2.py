import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        heapq.heapify(maxHeap)
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        for key,value in d.items():
            heapq.heappush(maxHeap, (-value, key))
        
        res = []
        for i in range(k):
            cur = heapq.heappop(maxHeap)
            res.append(cur[1])
        
        return res
