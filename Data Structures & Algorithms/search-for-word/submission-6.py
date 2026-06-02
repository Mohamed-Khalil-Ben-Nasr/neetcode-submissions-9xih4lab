class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        exists = False

        def dfs(row, col, i, s):
            # default cases
            # break if out of bounds or (row,col) cell has been already used
            if (row >= rows ) or (row < 0 ) or (col >= cols ) or (col < 0) or ((row,col) in s ) or (board[row][col] != word[i]):
                return False

            # return True because we found the word in the grid
            if i == len(word)-1 and board[row][col] == word[len(word)-1]:
                return True

            # mark this cell as visited
            s.add((row,col))
            # dfs over all directions
            directions = [[0,1], [0,-1], [1,0],[-1,0]]
            for dr, dc in directions:
                if dfs(row + dr,col + dc, i+1, s):
                    return True
            s.remove((row,col))
            return False
            

        for r in range(rows):
            for c in range(cols):
                # search for the word starting from any letter
                s = set()
                if dfs(r, c, 0, s):
                    exists = True
                    break
    
        return exists
