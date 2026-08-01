class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # brute force is O(4**(n**2)) because we are exploring all possible paths and we have to keep track of the current path max. therefore, dfs signature needs to be dfs(row,col, curPathMax) => no minimal state valid for memoization
        # => use a dijkstra variant since we start from a source and we are looking for the cheapest path to reach a destination
        # O(n**2 * log(n**2)) every cell in the grid is pushed and popped from minHeap

        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        minHeap = [[grid[0][0], (0,0)]]
        visited = set()
        while minHeap:
            # whenever we pop a cell, we are guaranteed that this is the cheapest cost to reach it
            curCost, coords = heapq.heappop(minHeap)
            # cell already visited via cheapest cost => skip
            if coords in visited:
                continue
            row,col = coords
            # dest reached via cheapest cost => return
            if row == rows-1 and col == cols-1:
                return curCost
            # mark current cell as visited
            visited.add(coords)
            # explore all 4 neighbors
            for dr,dc in dirs:
                r, c = row+dr, col+dc
                if r < 0 or c < 0 or r >= rows or c >= cols:
                    continue
                heapq.heappush(minHeap, [max(curCost, grid[r][c]), (r,c)])

            