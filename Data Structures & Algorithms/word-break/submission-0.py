class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(start):
            if start in dp:
                return dp[start]
            
            if start == len(s):
                return True

            dp[start] = False

            for word in wordDict:
                l = len(word)
                cur = s[start: start + l]
                if cur == word:
                    if dfs(start+l):
                        dp[start] = True
                        break

            return dp[start]

        return dfs(0)

        