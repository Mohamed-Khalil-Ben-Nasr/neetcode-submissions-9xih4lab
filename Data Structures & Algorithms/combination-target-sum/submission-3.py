class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            # base cases

            # valid solution
            # target reached
            if total == target:
                res.append(cur.copy())
                return

            # invalid solution
            # out of bounds or exceeded target
            if i >= len(nums) or total > target:
                return
            
            # branch 1: include nums[i]
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # branch 2: exclude nums[i]
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res