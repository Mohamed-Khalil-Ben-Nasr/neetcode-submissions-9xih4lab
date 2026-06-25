class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    def searchWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.addWord(word)

        res = set()
        visited = set()
        def dfs(row, col, cur, path, visited):
            # if out-of-bounds 
            # or current cell was already visited while exploring this path
            # or the current character doesnt belong to the word
            if (row < 0 or col < 0 or row >= rows or col >= cols
            or (row,col) in visited or board[row][col] not in cur.children):
                return
            
            # this cell is valid and contains a character thats part of a word in the Trie
            # => update cur
            cur = cur.children[board[row][col]]

            # mark this cell as visited
            visited.add((row,col))
            # update path
            path.append(board[row][col])

            if cur.endOfWord:
                word = "".join(path)
                res.add(word)

            # explore in all 4 dirs
            directions = [[0,1], [0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                dfs(row+dr, col+dc, cur, path, visited)
            # we finished exploring this cell
            # => pop from path to backtrack and remove from visited
            visited.remove((row,col))
            path.pop()
            return

        for row in range(rows):
            for col in range(cols):
                dfs(row,col, trie.root, [], visited)
        return list(res)













