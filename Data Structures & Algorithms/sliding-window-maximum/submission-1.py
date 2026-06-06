from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(len(nums)):
            # - pop from the front when index is out of bounds of the sliding window
            # => get rid of stale elements
            while q and q[0][0] < i-k+1:
                q.popleft()

            # - pop from the back when new element is greater
            # => maintain decreasing order
            while q and q[-1][1] < nums[i]:
                q.pop()

            q.append((i, nums[i]))

            # only append to res when we have enough elements for the sliding window
            if (i - k + 1 >= 0):
                res.append(q[0][1])

        return res