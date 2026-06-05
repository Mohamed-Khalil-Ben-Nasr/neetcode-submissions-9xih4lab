class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if rows == 1 and cols == 1:
            if obstacleGrid[rows-1][cols-1] == 0:
                return 1
            else:
                return 0
        dp = {}
        def dfs(r, c):
            if (r,c) in dp:
                return dp[(r,c)]
            if (r == rows-1 and c == cols-1):
                return 1
            if (r < 0 or c < 0 or r >= rows or c >= cols or obstacleGrid[r][c] == 1):
                return 0
            dp[(r,c)] = 0
            directions = [[1, 0], [0, 1]]
            for dr,dc in directions:
                dp[(r,c)] += dfs(r+dr, c+dc)
            return dp[(r,c)]

        return dfs(0,0)