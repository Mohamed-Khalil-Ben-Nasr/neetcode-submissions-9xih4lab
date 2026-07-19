class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        rows, cols = len(s1), len(s2)

        dp = [[False for j in range(cols+1)] for i in range(rows+1)]
        # base case => suffix is empty substrings
        dp[rows][cols] = True
        for i in range(rows, -1, -1):
            for j in range(cols, -1, -1):
                if i < rows and s1[i] == s3[i+j]:
                    dp[i][j] |= dp[i+1][j]
                
                if j < cols and s2[j] == s3[i+j]:
                    dp[i][j] |= dp[i][j+1] 
                    
        return dp[0][0]