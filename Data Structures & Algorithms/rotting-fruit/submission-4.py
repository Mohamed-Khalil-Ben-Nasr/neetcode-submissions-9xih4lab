from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0,-1],[1,0],[-1,0]]
        rottenQ = deque([])
        freshCount = 0
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rottenQ.append([row,col])
                    visited.add((row,col))
                if grid[row][col] == 1:
                    freshCount += 1
                    
        if freshCount == 0:
            return 0

        time = -1
        newRotten = 0
        while rottenQ:
            time += 1
            for i in range(len(rottenQ)):
                row,col = rottenQ.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col + dc
                    if (r < 0 or c < 0 or r >= rows or c >= cols
                    or (r,c) in visited or grid[r][c] == 0):
                        continue
                    newRotten += 1
                    grid[r][c] = 2
                    rottenQ.append([r,c])
                    visited.add((r,c))
            
        return time if newRotten == freshCount else -1