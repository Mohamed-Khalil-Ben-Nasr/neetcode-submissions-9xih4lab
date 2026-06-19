class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dp = {}
        def dfs(s, i):
            if (s,i) in dp:
                return dp[(s,i)]
            if i >= len(s):
                return 0
            dp[(s,i)] = float("-inf")
            for word in words:
                l = len(word)
                if s[i:i+l] == word:
                    cur = dfs(s, i+l)
                    if cur != float("-inf"):
                        dp[(s,i)] = max(dp[(s,i)],1 + cur)
            return dp[(s,i)]
        res = []
        for word in words:
            if dfs(word, 0) >= 2:
                res.append(word)
        return res