import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        numIslands = 0
        visited = set()

        def bfs(row,col):
            q = collections.deque()
            q.append([row,col])
            visited.add((row,col))
            while q:
                curR,curL = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    r, c = curR+dr, curL+dc
                    if (
                        r>-1 and
                        r<rows and
                        c>-1 and
                        c<cols and
                        grid[r][c] == "1" and
                        (r,c) not in visited
                    ):
                        visited.add((r,c))
                        q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=="1":
                    numIslands += 1
                    bfs(r,c)
        
        return numIslands
        