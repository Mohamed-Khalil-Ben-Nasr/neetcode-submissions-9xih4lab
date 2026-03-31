class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, s):
            # base cases
            if i > len(nums)-1 or s > target:
                return
            if s == target:
                # res.append(cur) only will store reference
                res.append(cur.copy())
                return
            
            # branching logic
            # branch where we add nums[i]
            cur.append(nums[i])
            dfs(i, cur, s+nums[i])

            # branch where we skip over nums[i]
            cur.pop()
            dfs(i+1, cur, s)
        
        dfs(0, [], 0)
        return res

        
