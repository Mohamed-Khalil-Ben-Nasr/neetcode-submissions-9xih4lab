class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        minHeap = [[grid[0][0], (0,0)]]
        visited = set()
        while minHeap:
            curCost, coords = heapq.heappop(minHeap)
            if coords in visited:
                continue
            row,col = coords
            if row == rows-1 and col == cols-1:
                return curCost
            visited.add(coords)
            for dr,dc in dirs:
                r, c = row+dr, col+dc
                if r < 0 or c < 0 or r >= rows or c >= cols:
                    continue
                heapq.heappush(minHeap, [max(curCost, grid[r][c]), (r,c)])

            