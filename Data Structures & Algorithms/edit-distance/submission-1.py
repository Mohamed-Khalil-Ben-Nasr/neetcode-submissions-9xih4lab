class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)
        dp = {}
        # subproblem: min num of ops to make w1[i:] into w2[j:]
        def dfs(i, j):
            # cache
            if (i,j) in dp:
                return dp[(i,j)]
            # base case -> empty string -> 0 ops
            if i == rows and j == cols:
                return 0
            # if w1 is exhausted
            if i == rows:
                return cols - j
            # if w2 is exhausted
            if j == cols:
                return rows - i

            dp[(i,j)] = 0
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1, j+1)
            else:
                # insert
                insert = dfs(i, j+1)
                # delete
                delete = dfs(i+1, j)
                # replace
                replace = dfs(i+1, j+1)
                dp[(i,j)] += 1 + min(insert, delete, replace)
            
            return dp[(i,j)]
        
        return dfs(0, 0)

