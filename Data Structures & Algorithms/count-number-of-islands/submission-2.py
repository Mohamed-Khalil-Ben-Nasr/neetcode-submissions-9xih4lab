from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        s = set()
        res = 0

        def dfs(row,col):
            # break if out-of-bounds or current cell is water 
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or grid[row][col] == "0"
                or (row,col) in s
            ):
                return
            # this current cell is part of the island
            # so mark it as visited
            s.add((row,col))
            # explore in all 4 directions
            directions = [[0,1], [0,-1], [1, 0],[-1,0]]
            for dr,dc in directions:
                dfs(row+dr, col+dc)
            # no need to backtrack because our set is for all visited lands
            # not just current path
            return

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in s:
                    # this is the start of a new island
                    # start exploring the island
                    dfs(row, col)
                    # increment number of islands
                    res += 1
        
        return res