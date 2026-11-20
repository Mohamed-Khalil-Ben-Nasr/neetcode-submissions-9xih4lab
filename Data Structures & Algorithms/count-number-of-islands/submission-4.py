class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0,1], [0,-1],[1,0],[-1,0]]
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(row, col):
            visited.add((row,col))
            q = deque([])
            q.append([row, col])
            while q:
                curRow, curCol = q.popleft()
                for dr, dc in dirs:
                    r, c = curRow + dr, curCol + dc
                    if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == "0"):
                        continue
                    visited.add((r, c))
                    q.append([r, c])
            return

        res = 0
        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col] == "1":
                    bfs(row, col)
                    res += 1
        return res