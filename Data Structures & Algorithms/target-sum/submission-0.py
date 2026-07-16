class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, cur):
            if (i,cur) in dp:
                return dp[(i,cur)]

            if i >= len(nums):
                if cur == target:
                    return 1
                else:
                    return 0
                    
            add = dfs(i+1, cur + nums[i])
            substract = dfs(i+1, cur - nums[i])
            dp[(i,cur)] = add + substract
            
            return dp[(i,cur)]
        return dfs(0, 0)
        
