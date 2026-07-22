class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        rows, cols = len(w1), len(w2)

        # current subproblem:
        # -> min number of ops to make w1[:i] to w2[:j]

        # or should it be including so each subprblem is min ways w1[:i+1] to w2[:j+1]
        dp = [[0 for col in range(cols+1)] for row in range(rows+1)]

        # base cases
        for i in range(rows+1):
            dp[i][0] = i
        
        for j in range(cols+1):
            dp[0][j] = j
    
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if w1[i-1] == w2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                # no match -> explore all ops and pick minimum
                delete = dp[i-1][j]
                replace = dp[i-1][j-1]
                insert = dp[i][j-1]
                dp[i][j] = 1 + min(delete, replace, insert)
        
        return dp[len(w1)][len(w2)]