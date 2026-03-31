import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows,cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            print(f"just added to visited ${r}${c}")
            while q:
                cr,cc = q.popleft()
                print(f" just popped from queue ${cr}${cc}")
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                # visit the neighbors
                for dr,dc in directions:
                    row,col = cr + dr, cc+dc
                    if (row > -1 and
                    col > -1 and
                    row < rows and
                    col < cols and
                    (row,col) not in visited and
                    grid[row][col] == "1"):
                        q.append((row,col))
                        visited.add((row,col))


        numIslands = 0
        for i in range(rows):
            for j in range(cols):
                if ((not ((i,j) in visited)) and (grid[i][j] == "1")):
                    print(f"${i,j}")
                    bfs(i,j)
                    numIslands += 1
                    
        
        return numIslands