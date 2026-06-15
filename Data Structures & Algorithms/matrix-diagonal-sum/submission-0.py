class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # its a square
        n = rows = cols = len(mat)
        visited = set()
        res = 0
        for row in range(rows):
            for col in range(cols):
                if (row == col) or (row + col == n-1) and (row,col) not in visited:
                    res += mat[row][col]
                    visited.add((row,col))

        return res