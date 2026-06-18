from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t
        
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        
        d1 = defaultdict(int)
        for c in t:
            d1[c] += 1
        
        for c in t:
            if (c not in d or d1[c] > d[c]):
                return c
        