class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:

        if t1 == "" or t2 == "":
            return 0

        rows, cols = len(t1), len(t2)
        dp = [[0] * (cols+1) for _ in range(rows+1)]
        for row in range(1,rows+1):
            for col in range(1,cols+1):
                if t1[row-1] == t2[col-1]: 
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        return dp[rows][cols]