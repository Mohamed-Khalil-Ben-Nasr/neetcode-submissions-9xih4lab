from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d1 = defaultdict(int)
        for c in chars:
            d1[c] += 1
        res = 0
        for word in words:
            good = True
            d2 = defaultdict(int)
            for c in word:
                d2[c] += 1
                if d2[c] > d1[c]:
                    good = False
                    break
            if good:
                res += len(word)
        return res
