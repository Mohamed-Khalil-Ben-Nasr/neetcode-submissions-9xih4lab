class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # subproblem: 
        # dp[(i,j)] => whether we were able to match s[:i] and p[:j]
        dp = {}
        def dfs(i, j):
            # base cases
            # cache hit
            if (i,j) in dp:
                return dp[(i,j)]

            # we matched all chars in s via p
            if i == len(s) and j == len(p):
                return True
            
            if j == len(p):
                return False
            
            # explore the decision tree
            dp[(i,j)] = False
            
            # we exhaust pattern and we still cant match all chars in s 
            # or exhaust all chars in s and cant reach the end of pattern
            if i < len(s):
                # wildcard or char match
                if p[j] == "." or s[i] == p[j]:
                    dp[(i,j)] |= dfs(i+1, j+1)


            if j+1 < len(p) and p[j+1] == "*":
                # repeat the preceding element 1 or more times
                if  i < len(s) and (p[j] == "." or s[i] == p[j]):
                    dp[(i,j)] |= dfs(i+1, j)

                # use it 0 times -> discard
                if j+2 <= len(p):
                    dp[(i,j)] |= dfs(i, j+2)

            return dp[(i,j)]
        
        return dfs(0,0)
            

            

            
                
                
            
