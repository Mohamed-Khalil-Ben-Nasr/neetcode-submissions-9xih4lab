class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return
            # include
            cur.append(nums[i])
            dfs(i+1, cur)
            # exclude
            # if we exclude then include a duplicate again
            # => we will have duplicate subsets
            # => so we need to exclude all duplicates
            cur.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, cur)
            return 
        dfs(0, [])
        return res
