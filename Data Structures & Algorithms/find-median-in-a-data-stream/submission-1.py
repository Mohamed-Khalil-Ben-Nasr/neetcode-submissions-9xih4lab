class MedianFinder:

    def __init__(self):
        # small is max heap
        self.small = []
        # large is min heap
        self.large = []

    def addNum(self, num: int) -> None:
        # O(log n)
        heapq.heappush(self.small, -num)

        # invariant 1: every element in small <= every element in large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # invariant 2: difference in lengths between the two halves/heaps cant exceed 1
        if len(self.small) > len(self.large) + 1:
            # pop max from small
            val = -1 * heapq.heappop(self.small)
            # add it to large
            heapq.heappush(self.large, val)

        elif len(self.large) > len(self.small) + 1:
            # pop min from large
            val = heapq.heappop(self.large)
            # add it to small
            heapq.heappush(self.small, -1 * val)

        # => now the sizes of both heaps are balanced
        # no need for while loop because the moment the diff hits 2, we rebalance

    def findMedian(self) -> float:
        # O(1)
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2
        