import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        heapq.heapify(self.heap)
        self.k = k
        for num in nums:
            heapq.heappush(self.heap, num)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        print(self.heap)
        
    def add(self, val: int) -> int:
        print("add ", 3)
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
        
