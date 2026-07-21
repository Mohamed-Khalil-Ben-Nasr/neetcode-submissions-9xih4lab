class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        unresolvedGreater = [[0 for j in range(cols)] for i in range(rows)]
        q = deque([])
        for row in range(rows):
            for col in range(cols):
                for dr, dc in dirs:
                    r, c = row+dr, col+dc
                    if (r < 0 or c < 0 or r >= rows or c >= cols
                    or matrix[r][c] <= matrix[row][col]):
                        continue
                    unresolvedGreater[row][col] += 1
                if unresolvedGreater[row][col] == 0:
                    q.append([row,col])
        res = 1
        dp = [[1 for j in range(cols)] for i in range(rows)]
        while q:
            row,col = q.popleft()
            print("row ", row, " col ", col)
            LIP = 0
            for dr, dc in dirs:
                r, c = row+dr, col+dc
                # out of bounds
                if (r < 0 or c < 0 or r >= rows or c >= cols 
                or matrix[r][c] == matrix[row][col]):
                    continue
                # smaller neighbor => update uncresolvedGreater[smaller]
                if matrix[r][c] < matrix[row][col]: 
                    unresolvedGreater[r][c] -= 1
                    # all unresolvedGreater[smaller] have been processed
                    # => we can process smaller
                    if unresolvedGreater[r][c] == 0:
                        q.append([r,c])
                    continue
                # greater neighbor => update current dp[row][col]
                LIP = max(LIP, dp[r][c])
            print("LIP ", LIP)
            dp[row][col] += LIP
            res = max(res, dp[row][col])
        print(dp)
        return res
            
                
                    