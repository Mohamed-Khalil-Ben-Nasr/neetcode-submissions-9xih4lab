class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # first balloon bursted approach: 
        # we need to explore all possible order permutations => O(n!)
        # no valid minimal state to memoize

        # Last balloon bursted approach: 
        # subproblem 
        # max coins received by bursting all balloons in each subarray n**2
        # for each subarray, we consider each ballon k as the last burted n
        # the neighbors of each subarray are fixed
        # => space complexity O(n**2) and O(n**3) time complexity
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l,r)]

            dp[(l,r)] = 0
            # consider each ballon k as the last bursted balloon
            for k in range(l, r+1):
                cur = nums[l-1] * nums[k] * nums[r+1] 
                cur += dfs(l,k-1) + dfs(k+1, r)
                dp[(l,r)] = max(dp[(l,r)], cur)

            return dp[(l,r)]


        return dfs(1, len(nums)-2)

