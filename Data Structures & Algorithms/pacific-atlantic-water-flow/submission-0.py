class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, visited, prevHeight):
            # base cases
            # break if out-of-bounds or cell already visited or value less than prevHeight
            if (
                row < 0 or col < 0 or row >= rows or col >= cols
                or (row,col) in visited or heights[row][col] < prevHeight
            ):
                return
            # this is a valid cell 
            visited.add((row,col))
            # dfs in all directions
            directions = [[0,1], [0,-1], [1,0],[-1,0]]
            for dr,dc in directions:
                dfs(row+dr, col+dc, visited, heights[row][col])
            return

        
        for r in range(rows):
            # visit all cells that reach the pacific 
            dfs(r, 0, pacific, heights[r][0])
            # visit all cells that reach the atlantic
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        for c in range(cols):
            # visit all cells that reach the pacific 
            dfs(0, c, pacific, heights[0][c])
            # visit all cells that reach the atlantic
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if ((r,c) in atlantic and (r,c) in pacific):
                    res.append([r,c])
        return res

