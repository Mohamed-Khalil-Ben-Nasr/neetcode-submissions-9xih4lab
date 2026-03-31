class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return True
        
        return False