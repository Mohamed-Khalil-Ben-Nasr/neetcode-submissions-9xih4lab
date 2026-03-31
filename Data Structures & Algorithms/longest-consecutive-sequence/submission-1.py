class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        l = 1
        for num in s:
            if (num-1) in s:
                continue
            curL = 1
            start = num
            while (start + 1) in s:
                curL += 1
                start += 1
            l = max(curL, l)
        
        return l