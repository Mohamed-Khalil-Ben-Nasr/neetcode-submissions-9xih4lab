class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for num in seen:
            if num-1 in seen:
                continue
            cur = num
            l = 1
            while cur+1 in seen:
                cur += 1
                l += 1
            res = max(res, l)
        return res