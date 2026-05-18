from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def generateDict(s : str):
            d = defaultdict(int)
            for c in s:
                d[c] += 1
            return d
        
        if len(s) != len(t):
            return False

        d1 = generateDict(s)
        d2 = generateDict(t)
        for key in d1.keys():
            if d1[key] != d2[key]:
                return False
        
        return True