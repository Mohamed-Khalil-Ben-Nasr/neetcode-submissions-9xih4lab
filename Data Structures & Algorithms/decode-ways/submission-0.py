class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        def dfs(i):
            if i == len(s):
                return 1
            if dp[i] != 0:
                return dp[i]
            if s[i] == "0":
                return 0
            
            if i+1 <= len(s) and 0 < int(s[i]) <= 9:
                dp[i] += dfs(i+1)
            if i+2 <= len(s) and 0 < int(s[i:i+2]) <= 26:
                dp[i] += dfs(i+2)
            return dp[i]
        return dfs(0)