class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        partition = []
        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            for j in range(i, len(s)):
                if isPali(i, j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
        dfs(0)
        return res