class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # at first, it seems that we need to do round trip
        # however, starting from (n-1, n-1) and going up or left 
        # is the equivalent of starting from (0,0) and going down or right
        # therefore, the problem becomes the maximum cherries collected 
        # by 2 people who start from (0,0) and can move either down or right
        # a cherry in a cell can only be picked once
        # so when the 2 meet at a cherry with a cell, we can only do +1 instead of +2
        # i see so they are always synchronized and take the same number of steps and 
        # in a nxn grid, to reach the n-1,n-1 going either down or right u need to 
        # take 2(n-1) steps (the most direct path and shortest path is 2(n-1) 
        # and if one of them goes out of bounds that means this case is definitely 
        # not the maximum they can both collect and 
        # a solution is only valid if they reach the endpoint at the same time
        rows = cols = len(grid)
        dp = {}
        def dfs(r1, c1, r2, c2):
            # base cases
            # if this state was already computed
            if (r1, c1, r2, c2) in dp:
                return dp[ (r1, c1, r2, c2) ]
            # if out-of-bounds or reached a thorn
            if (
                r1 < 0 or c1 < 0 or r2 < 0 or c2 < 0
                or r1 >= rows or c1 >= cols or r2 >= rows or c2 >= cols
                or grid[r1][c1] == -1 or grid[r2][c2] == -1 
            ):
                return float("-inf")
            # if they both reached the bottom right of the grid
            if (r1 == rows-1 and r2 == rows-1 and c1 == cols-1 and c2 == cols-1):
                return grid[rows-1][cols-1]
            # time to let the two dogs out
            if (r1 == r2 and c1 == c2):
                dp[(r1, c1, r2, c2)] = grid[r1][c1]
            else:
                dp[(r1, c1, r2, c2)] = grid[r1][c1] + grid[r2][c2]
            res = float("-inf")
            # if they both go right
            res = max(res, dfs(r1,c1+1,r2,c2+1))
            # if they both go down
            res = max(res, dfs(r1+1,c1,r2+1,c2))
            # if one down and one right
            res = max(res, dfs(r1+1,c1,r2,c2+1))
            # opposite
            res = max(res, dfs(r1,c1+1,r2+1,c2))
            dp[(r1, c1, r2, c2)] += res
            return dp[(r1, c1, r2, c2)]
        res = dfs(0,0,0,0)
        return res if res != float("-inf") else 0