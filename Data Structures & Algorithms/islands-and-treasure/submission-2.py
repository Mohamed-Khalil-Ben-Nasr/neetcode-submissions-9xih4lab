from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        q = deque([])
        visited = set()
        # seed the queue with treasure cells positions
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append([row,col])
                    visited.add((row,col))
        # start multi-source-bfs
        # invariant => "shortest path from nearest treasure"
        level = 1
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r < 0 or c < 0 
                    or r >= rows or c >= cols
                    or (r,c) in visited
                    or grid[r][c] == -1):
                        continue
                    grid[r][c] = level
                    q.append([r,c])
                    visited.add((r,c))
            level += 1
        