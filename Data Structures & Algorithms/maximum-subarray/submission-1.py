class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = float("-inf")
        curS = 0
        for num in nums:
            curS += num
            m = max(m, curS)
            if curS < 0:
                # restart counting the sum from the next element
                curS = 0
                continue
        return m