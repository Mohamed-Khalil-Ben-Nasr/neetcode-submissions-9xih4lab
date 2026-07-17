class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # time complexity: O(len(s1) * len(s2)) 
        # => we could recurse through all possible combinations
        # space complexity = mem dict size = O(len(S1) * len(S2))
        # stack depth => O(len(s1) + len(s2)) 
        # => need to recurse max len(S3) times to construct s3

        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        def dfs(i , j):
            # cache hit
            if (i, j) in dp:
                return dp[(i,j)]

            # we consumed all chars of s1 and s2 
            # and we created s3 successfully
            if i + j == len(s3):
                return True

            dp[(i,j)] = False
            # if double match
            # => explore both choices
            # => cant use greedy approach 
            # or we risk not exploring the valid path
            if i < len(s1) and s1[i] == s3[i+j]:
                dp[(i,j)] = dp[(i,j)] or dfs(i+1, j)

            if j < len(s2) and s2[j] == s3[i+j]:
                dp[(i,j)] = dp[(i,j)] or dfs(i, j+1)

            # else => no match 
            # => invalid path => dp entry stays False
            return dp[(i,j)]
            
        return dfs(0,0)