class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        rows, cols = len(w1), len(w2)
        dp = [[0 for j in range(cols+1)] for i in range(rows+1)]
        for i in range(rows+1):
            dp[i][cols] = rows-i
        
        for j in range(cols+1):
            dp[rows][j] = cols-j
        
        dp[rows][cols] = 0
        
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1,-1):
                if w1[i] == w2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    # insert
                    insert = dp[i][j+1]

                    # delete
                    delete = dp[i+1][j]

                    # replace
                    replace = dp[i+1][j+1]

                    dp[i][j] = 1 + min(insert, delete, replace)
        return dp[0][0]