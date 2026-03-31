import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        ds = collections.defaultdict(int)
        dt = collections.defaultdict(int)
        for c in s:
            ds[c] = ds.get(c, 0) + 1
        
        for c in t:
            dt[c] = dt.get(c, 0) + 1
        
        for c in s:
            if ds[c] != dt[c]:
                return False
        
        return True