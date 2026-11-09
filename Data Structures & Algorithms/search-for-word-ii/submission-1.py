class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.word = ""

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        cur.word = word
        return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = PrefixTree()
        for word in words:
            tree.insert(word)

        dirs = [[0,1], [0,-1], [1,0],[-1,0]]
        res = set()
        visited = set()
        rows, cols = len(board), len(board[0])

        def dfs(row, col, curNode, visited):
            if curNode.endOfWord:
                res.add(curNode.word)

            for dr, dc in dirs:
                r, c = row+dr, col+dc
                if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or board[r][c] not in curNode.children):
                    continue
                visited.add((r, c))
                dfs(r, c, curNode.children[board[r][c]], visited)
                visited.remove((r,c))
            
            return

        for row in range(rows):
            for col in range(cols):
                if board[row][col] not in tree.root.children:
                    continue
                visited.add((row, col))
                dfs(row, col,tree.root.children[board[row][col]], visited)
                visited.remove((row,col))
                
        return list(res)