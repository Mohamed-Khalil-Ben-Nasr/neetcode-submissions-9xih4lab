class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}
        def dfs(r, c):
            if (r,c) in mem:
                return mem[(r,c)]
            if (r == m-1 and c == n-1):
                return 1
            if (r < 0 or c < 0 or r >= m or c >= n):
                return 0
            # u can only move down or to the right
            directions = [[0,1], [1,0]]
            mem[(r,c)] = 0
            for dr,dc in directions:
                mem[(r,c)] += dfs(r+dr, c+dc)
            return mem[(r,c)]

        return dfs(0, 0)