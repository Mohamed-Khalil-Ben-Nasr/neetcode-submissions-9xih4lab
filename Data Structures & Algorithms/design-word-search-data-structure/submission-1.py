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
        def dfs(curNode, i):
            # base case: success
            if i == len(word):
                return curNode.endOfWord

            # explore children
            # if current letter is "." => explore all children
            if word[i] == ".":
                for c in curNode.children:
                    if dfs(curNode.children[c], i+1):
                        return True
                return False
            else:
            # current letter is a regular letter => explore the matching path
                if word[i] not in curNode.children:
                    return False
                return dfs(curNode.children[word[i]], i+1)
 
        return dfs(self.root, 0)
