class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        visited.add((0,0))
        row, col = 0,0
        dirs = {'N': [-1,0], 'S': [1,0], 'E': [0,1], 'W':[0,-1]}
        for c in path:
            dr, dc = dirs[c]
            row += dr
            col += dc
            if (row,col) in visited:
                return True
            visited.add((row,col))
        return False
            