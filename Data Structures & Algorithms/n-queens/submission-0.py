class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows, cols = n, n
        occupiedCols, occupiedDiagonals, occupiedAntiDiagonals = set(), set(), set()
        currentQueensPositions = []
        res = []
        def dfs(row):
            # we finished placing all queens
            if row == n:
                # get snapshot of queens positions on current board solution
                res.append(currentQueensPositions.copy())
                return
            for col in range(cols):
                if (col not in occupiedCols
                and row + col not in occupiedDiagonals
                and row - col not in occupiedAntiDiagonals):
                    # we can put a queen here
                    occupiedCols.add(col)
                    occupiedDiagonals.add(row+col)
                    occupiedAntiDiagonals.add(row-col)
                    currentQueensPositions.append(col)
                    dfs(row+1)
                    # pop since we finished exploring this path
                    # to backtrack
                    occupiedCols.remove(col)
                    occupiedDiagonals.remove(row+col)
                    occupiedAntiDiagonals.remove(row-col)
                    currentQueensPositions.pop()
            return
        dfs(0)
        print(res)
        finalRes = []
        for solution in res:
            currentSolution = []
            for queenCol in solution:
                row = ["." for i in range(n)]
                row[queenCol] = 'Q'
                currentSolution.append("".join(row))
            finalRes.append(currentSolution)
        return finalRes



            