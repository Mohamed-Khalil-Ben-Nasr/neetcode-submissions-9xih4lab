from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0,-1],[1,0], [-1,0]]
        def bfs(row, col):
            print("bfs row ", row, " col ", col)
            q = deque()
            visited = set()
            q.append([row, col])
            level = 1
            while q:
                for i in range(len(q)):
                    row,col = q.popleft()
                    visited.add((row,col))
                    for dr,dc in directions:
                        r, c = row + dr, col + dc
                        if (r < 0 or c < 0 or r >= rows or c >= cols
                        or (r,c) in visited or grid[r][c] == -1
                        or grid[r][c] == 0):
                            continue
                        grid[r][c] = min(grid[r][c], level)
                        q.append([r,c])
                level += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    bfs(row,col)