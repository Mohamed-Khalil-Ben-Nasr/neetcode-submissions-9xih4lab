class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patternToWords = defaultdict(set)
        wordToPatterns = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            pattern = []
            for c in word:
                pattern.append(c)
            for i in range(len(word)):
                newPattern = pattern.copy()
                newPattern[i] = "*"
                newP = "".join(newPattern)
                patternToWords[newP].add(word)
                wordToPatterns[word].append(newP)
        q = deque([])
        visited = set()
        q.append(beginWord)
        visited.add(beginWord)
        res = 0
        while q:
            res += 1
            for i in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for pattern in wordToPatterns[cur]:
                    for word in patternToWords[pattern]:
                        if word not in visited:
                            visited.add(word)
                            q.append(word)
        return 0

        