class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        dp = {}
        rows, cols = len(t1), len(t2)
        def dfs(i, j):
            # memoization
            if (i,j) in dp:
                return dp[(i,j)]
            # base cases
            if (i < 0 or j < 0 or i >= rows or j >= cols):
                return 0
            # if there is a match
            if t1[i] == t2[j]:
                dp[(i,j)] = 1 + dfs(i+1, j+1)
            else:
                dp[(i,j)] = max(dfs(i+1,j), dfs(i, j+1))
            return dp[(i,j)]
        return dfs(0,0)