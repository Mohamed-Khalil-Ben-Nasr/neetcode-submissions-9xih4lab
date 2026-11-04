class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = defaultdict(int)
        for c in s:
            d1[c] += 1
        
        d2 = defaultdict(int)
        for c in t:
            d2[c] += 1
        
        for k in d1.keys():
            if d1[k] != d2[k]:
                return False
            
        return True