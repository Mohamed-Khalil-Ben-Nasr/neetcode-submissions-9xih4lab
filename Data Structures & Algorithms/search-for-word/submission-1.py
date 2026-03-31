class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # to make sure that the same cell is not used more than once in our path
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            # remember that we are going to look for the word in all 4 directions
            if (r<0 
            or c<0 
            or r>=rows 
            or c>=cols
            or board[r][c] != word[i]
            or ((r,c) in path)):
                return False

            # add tuple (r,c) to mark cell as visited
            path.add((r,c))
            
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            # remove the current cell from path since we finished using it
            # so that we can still reuse it
            path.remove((r,c))

            return res
    
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        
        return False
    
