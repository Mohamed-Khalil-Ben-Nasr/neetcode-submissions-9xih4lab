from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = cols = 9
        rowToCells = defaultdict(set)
        colToCells = defaultdict(set)
        squareToCells = defaultdict(set)

        for row in range(rows):
            for col in range(cols):
                val = board[row][col]
                if val == ".":
                    continue
                val = int(val)
                if (val in rowToCells[row] 
                or val in colToCells[col]
                or val in squareToCells[(row//3, col//3)]):
                    return False
                rowToCells[row].add(val)
                colToCells[col].add(val)
                squareToCells[(row//3, col//3)].add(val)
        return True