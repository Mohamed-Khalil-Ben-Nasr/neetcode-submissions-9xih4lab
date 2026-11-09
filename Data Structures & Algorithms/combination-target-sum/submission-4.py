class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, comb):
            nonlocal res

            if total == target:
                res.append(comb.copy())
                return
            
            if total > target or i >= len(nums):
                return
            
            # reuse/include nums[i]
            comb.append(nums[i])
            dfs(i, total+ nums[i], comb)

            # exclude nums[i]
            comb.pop()
            dfs(i+1, total, comb)

            return
        
        dfs(0, 0, [])
        return res
