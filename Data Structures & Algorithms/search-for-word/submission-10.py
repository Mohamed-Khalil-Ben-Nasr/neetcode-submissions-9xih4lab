class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()
        
        def dfs(row, col, i, visited):
            if i == len(word)-1 and board[row][col] == word[i]:
                return True
            
            if board[row][col] != word[i]:
                return False

            for dr, dc in dirs:
                r, c = row+dr, col+dc
                if (r < 0 or c < 0 or r >= rows or c >= cols 
                or (r,c) in visited or board[r][c] != word[i+1]):
                    continue
                visited.add((r, c))
                if dfs(r, c, i+1, visited):
                    return True
                visited.remove((r, c))

            return False


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    visited.add((row, col))
                    if dfs(row, col, 0, visited):
                        return True
                    visited.remove((row,col))

        return False
