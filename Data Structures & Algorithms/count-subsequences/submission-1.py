class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        rows, cols = len(s)+1, len(t)+1
        # subproblem:
        # number of distinct ways to create t[j:]
        # from chars in substring s[i:]
        dp = [[0 for col in range(cols)] for row in range(rows)]
        # base case 
        # => empty subsequence t[len(t):] from empty substring s[len(s):]
        dp[len(s)][len(t)] = 1
        # iteration order needs to respect dependency resolution
        # => in this case, a simple bottom right to top left 
        # iteration suffices
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                # include 
                if (i + 1 < rows and j + 1 < cols and s[i] == t[j]):
                    dp[i][j] += dp[i+1][j+1]
                # exclude
                if (i + 1 < rows):
                    dp[i][j] += dp[i+1][j]
        return dp[0][0]
                

