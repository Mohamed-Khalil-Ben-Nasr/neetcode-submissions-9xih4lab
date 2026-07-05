class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # the hard part is tracking the options that are left 
        # after making a choice in the decision tree
        # the workaround is to simply track whats already been used
        # then we can represent the options left cleanly in code
        res = []
        def dfs(cur, s):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for num in nums:
                if num not in s:
                    s.add(num)
                    cur.append(num)
                    dfs(cur, s)
                    # backtrack to explore other options in the same level
                    s.remove(num)
                    cur.pop()
            return
        dfs([], set())
        return res

            