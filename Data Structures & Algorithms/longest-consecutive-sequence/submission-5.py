class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxL = 0
        curMax = 0
        for num in nums:
            if num-1 in nums:
                continue

            cur = num
            curMax = 1
            while cur+1 in nums:
                curMax += 1
                cur += 1
            
            maxL = max(curMax, maxL)
        
        return maxL