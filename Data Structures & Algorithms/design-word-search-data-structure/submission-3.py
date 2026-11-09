class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        return

    def search(self, word: str) -> bool:
        
        def searchHelper(cur, i):
            if (i == len(word)):
                return cur.endOfWord
            
            if (word[i] == '.'):
                for child in cur.children.values():
                    if searchHelper(child, i+1):
                        return True
                return False
            else:
                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
                return searchHelper(cur, i+1)
        
        return searchHelper(self.root, 0)
