class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [[0,1], [0,-1],[1,0],[-1,0]]
        visited = set()
        dp = {}
        def dfs(row, col, prev):
            if (row < 0 or col < 0 
            or row >= rows or col >= cols
            or (row,col) in visited
            # even if (row,col) in dp
            # if its smaller than prev, then it cant be 
            # a continuation of the LIP sequence
            or matrix[row][col] <= prev):
                return 0
            # matrix[row][col] can be a continuation of the sequence
            if (row,col) in dp:
                return dp[(row,col)]
            # mark current cell as visited
            visited.add((row,col))
            # explore
            res = 0
            for dr,dc in directions:
                cur = dfs(row+dr, col+dc, matrix[row][col])
                res = max(res, cur)
            # pop so that we can backtrack and explore other branches
            visited.remove((row,col))
            dp[(row, col)] = res + 1
            return dp[(row, col)]
        res = 0
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                res = max(res, dfs(row,col, -1))
                
        return res