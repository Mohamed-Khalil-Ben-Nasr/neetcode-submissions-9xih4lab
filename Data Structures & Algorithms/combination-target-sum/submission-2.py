class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, total, cur):
            if i < len(nums) and total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i, total+nums[i], cur)
            cur.pop()
            dfs(i+1, total, cur)
        
        dfs(0, 0, [])
        return res