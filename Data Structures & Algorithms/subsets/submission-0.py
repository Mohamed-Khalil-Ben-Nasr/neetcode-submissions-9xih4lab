class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, subset):
            nonlocal res
            # if there is no new element to consider
            if i == len(nums):
                res.append(subset.copy())
                return
            # options: either include/exclude current element
            # we can have duplicate num
            # => 0/1 bounded knapsack
            # include
            subset.append(nums[i])
            dfs(i+1, subset)
            # exclude
            subset.pop()
            dfs(i+1, subset)
            return
        
        dfs(0, [])
        return res
