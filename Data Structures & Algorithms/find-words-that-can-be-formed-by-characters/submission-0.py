from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d1 = defaultdict(int)
        for c in chars:
            d1[c] += 1
        res = 0
        for word in words:
            d2 = defaultdict(int)
            for c in word:
                d2[c] += 1
            formed = True
            for c in d2:
                # we dont have enough
                if d2[c] > d1[c]:
                    formed = False
            if formed:
                res += len(word)
        return res
