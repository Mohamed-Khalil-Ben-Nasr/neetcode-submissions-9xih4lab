class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(row, col):
            if (row < 0 or col < 0 
            or row >= rows or col >= cols
            or (row, col) in visited
            or grid[row][col] == 0):
                return 0
            visited.add((row,col))
            curArea = 1
            directions = [[0, 1], [0, -1], [1,0], [-1,0]]
            for dr,dc in directions:
                curArea += dfs(row + dr, col+dc)
            return curArea
        
        res = 0
        for row in range(rows):
            for col in range(cols):
                if ( grid[row][col] == 1 and (row,col) not in visited):
                    area = dfs(row,col)
                    res = max(res, area)
        return res