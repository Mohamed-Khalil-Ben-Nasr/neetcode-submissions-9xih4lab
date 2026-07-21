class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # by drawing out the decision tree, we can reach the same dfs(i,j)
        # from different paths
        # => add memoization
        dp = {}
        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i,j)]

            # we created subsequence t from chars in s[:i]
            # => success
            if j == len(t):
                return 1

            # we processed all chars in s but couldnt create a subsequence == t
            # => failure
            if i == len(s):
                return 0
            
            # explore:
            include = 0
            # only include if there is a match
            if s[i] == t[j]:
                include = dfs(i+1, j+1)

            # always exclude
            exclude = dfs(i+1, j)
            dp[(i,j)] = include + exclude

            return dp[(i,j)]
        return dfs(0, 0)




            
