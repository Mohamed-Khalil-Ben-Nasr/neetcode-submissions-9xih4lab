class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [[0,1], [0,-1],[1,0],[-1,0]]

        def dfs(row, col, visited):
            visited.add((row, col))
            for dr, dc in dirs:
                r, c = row+dr, col+dc
                if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or heights[row][col] > heights[r][c]):
                    continue
                dfs(r, c, visited)
        
        atl, pac = set(), set()
        for row in range(rows):
            dfs(row, 0, pac)
            dfs(row, cols-1, atl)
        
        for col in range(cols):
            dfs(0, col, pac)
            dfs(rows-1, col, atl)
        
        res = []
        for row in range(rows):
            for col in range(cols):
                if (row,col) in atl and (row,col) in pac:
                    res.append([row, col])
        
        return res
