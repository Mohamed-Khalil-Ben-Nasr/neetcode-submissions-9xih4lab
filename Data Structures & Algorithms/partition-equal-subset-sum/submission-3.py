class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        
        if total % 2:
            # odd
            return False

        half = total / 2
        # time complexity O(2 ** n) => exponential => hits TLE
        # => need to memoize
        # => dp[(i, (s1, s2))]
        # => the memoization table size is too big + this doesnt mark 
        # example dp[(i, (2, 1))] and dp[(i, (1,2))] as collision
        # => s1 + s2 = sum(nums[:i+1])
        # => notice that s2 is derivable from s1
        # => dp[(i, s1)]
        # => space complexity O(100 * 50 * 100) => polynomial => better

        dp = {}
        def dfs(i, s1):
            if (i, s1) in dp:
                return dp[(i, s1)]

            if i == len(nums):
                return s1 == half

            # decision tree
            # choice 1: add nums[i] to s1
            dec1 = dfs(i+1, s1+nums[i])
            # choice 2: add nums[i] to s2
            dec2 = dfs(i+1, s1)
            dp[(i, s1)] = dec1 or dec2
            return dp[(i, s1)] 
        
        return dfs(0, 0)
            
