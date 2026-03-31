class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if (total == target):
                # success -> add current combination to solutions array (res)
                res.append(cur.copy())
                return
            if ((total > target) or (i >= len(nums))):
                # break
                return
            # so in the decision tree, we explore combinations 
            # where we either add the current num or skip it

            # add the current nums[i]
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # pop it to explore the decision tree where we dont add it
            cur.pop()
            dfs(i+1, cur, total)

        dfs( 0, [], 0)
        return res