class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # there is m*n cells/different states, and each state result is 
        # computed only once thanks to memoization
        # => time complexity = O(m*n)
        # space complexity = memo dict space = O(m*n)
        # max recursion depth = O(m*n) since it can be one
        # long sequence spanning every cell in the table
        rows, cols = len(matrix), len(matrix[0])
        directions = [[0,1], [0,-1],[1,0],[-1,0]]
        dp = {}
        def dfs(row, col):
            # matrix[row][col] can be a continuation of the sequence
            if (row,col) in dp:
                return dp[(row,col)]
            # explore
            res = 0
            for dr,dc in directions:
                r, c = row+dr, col+dc
                if (r < 0 or c < 0 or r >= rows or c >= cols
                or matrix[r][c] <= matrix[row][col]):
                    continue
                cur = dfs(r, c)
                res = max(res, cur)
            dp[(row, col)] = res + 1
            return dp[(row, col)]
        # memoization eliminates repeated work, but cannot not reduce 
        # necessary recursion depth
        res = 0
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                res = max(res, dfs(row,col))
                
        return res