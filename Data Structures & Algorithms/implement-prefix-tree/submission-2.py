class TrieNode:
    def __init__(self):
        self.val = None
        self.children = {}
        self.wordEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        prev = self.root
        for c in word:
            if c in prev.children:
                prev = prev.children[c]
                continue
            cur = TrieNode()
            cur.val = c
            prev.children[c] = cur
            prev = cur

        prev.wordEnd = True
        return

    def search(self, word: str) -> bool:
        i = 0
        cur = self.root
        while i < len(word):
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]
            i += 1
        return cur.wordEnd

    def startsWith(self, prefix: str) -> bool:
        i = 0
        cur = self.root
        while i < len(prefix):
            if prefix[i] not in cur.children:
                return False
            cur = cur.children[prefix[i]]
            i += 1
        return True
         