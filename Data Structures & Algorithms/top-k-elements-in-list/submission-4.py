import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = defaultdict(int)
        for num in nums:
            numToFreq[num] += 1

        maxHeap = []
        for num, freq in numToFreq.items():
            heapq.heappush(maxHeap, [-freq, num])
        
        res = []
        while k > 0:
            negFreq, num = heapq.heappop(maxHeap)
            res.append(num)
            k -= 1
        
        return res