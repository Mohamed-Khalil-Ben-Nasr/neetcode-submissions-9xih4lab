class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        m = 0
        l = 0
        for num in nums:
            cur = num
            while cur in nums:
                l += 1
                cur += 1
            m = max(m,l)
            l = 0
        
        return m