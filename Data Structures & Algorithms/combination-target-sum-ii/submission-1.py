class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, total):
            # base cases
            # success
            if total == target:
                res.append(cur.copy())
                return

            # failure
            if i >= len(candidates) or total > target:
                return

            # decision branches:
            # add current candidates[i] to the combination
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            # dont consider candidates[i] in the current combination
            # if we exclude current element in dfs(i) 
            # then include the same element in dfs(i+1)
            # => we will reproduce a duplicate solution
            # so when we exclude current element, we need to also exclude all of its occurences
            # => find the first different element after all occurences of current element
            cur.pop()
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            dfs(i, cur, total)
            return
        dfs(0, [], 0)
        return res