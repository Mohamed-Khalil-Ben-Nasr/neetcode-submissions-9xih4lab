class MedianFinder:

    def __init__(self):
        self.small = []
        heapq.heapify(self.small)
        self.large = []
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        # decide where to push NUM

        # push by default to small heap first
        heapq.heappush(self.small, -1 * num)

        # maintain the invariant: max(small) <= min(large)
        if (self.small and self.large and 
        (-self.small[0] > self.large[0])):
            # pop from small
            v = -1 * heapq.heappop(self.small)
            # push to large
            heapq.heappush(self.large, v)
        
        # rebalance the heaps if the difference in lengths exceeds 1
        if (len(self.small) - len(self.large) > 1):
            # pop from small
            v = -1 * heapq.heappop(self.small)
            # push to large
            heapq.heappush(self.large, v)
        if (len(self.large) - len(self.small) > 1):
            # pop from large
            v = heapq.heappop(self.large)
            # push to small
            heapq.heappush(self.small, -1 * v)

        print("we added ", num)
        print("small heap: ", self.small)
        print("large heap: ", self.large)
    def findMedian(self) -> float:
        # if the total number of elements is odd
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        # if the total number of elements is even
        else:
            return ((self.small[0]* -1 + self.large[0]) / 2)
        
        