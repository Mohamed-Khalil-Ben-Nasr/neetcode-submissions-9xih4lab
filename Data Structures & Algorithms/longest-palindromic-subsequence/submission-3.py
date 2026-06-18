# python default recursion limit is 1000, 
# but if a string is 1000, there will be 1000+ recursion
import sys
sys.setrecursionlimit(10000)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # longest palindromic subsequence in s is basically
        # LCS of s and reversed_s
        r = s[::-1]
        dp = {}
        n = len(s)
        def dfs(i,j):
            # base cases
            if (i,j) in dp:
                return dp[(i,j)]
            # if out-of-bounds
            if (i < 0 or j < 0 or i >= n or j >= n):
                return 0
            # if chars match
            if s[i] == r[j]:
                dp[(i,j)] = 1 + dfs(i+1, j+1)
            else:
                dp[(i,j)] = max(dfs(i+1,j), dfs(i, j+1))
            return dp[(i,j)]
        return dfs(0,0)


