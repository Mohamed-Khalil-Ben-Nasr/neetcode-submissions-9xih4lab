class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        def dfs(row,col):
            if (row < 0 or col < 0 or row >= rows or col >= cols 
            or board[row][col] == "X" 
            or board[row][col] == "E"):
                return
            board[row][col] = "E"
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in directions:
                dfs(row+dr, col+dc)
            return
        
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)
            if board[rows-1][col] == "O":
                dfs(rows-1, col)
        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][cols-1] == "O":
                dfs(row,cols-1)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "E":
                    board[row][col] = "O"

        