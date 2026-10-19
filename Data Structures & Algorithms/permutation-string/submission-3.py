class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        d1 = defaultdict(int)
        for c in s1:
            d1[c] += 1

        l = 0
        d2 = defaultdict(int)
        for r in range(len(s2)):
            d2[s2[r]] += 1
            if (r - l + 1) < len(s1):
                continue
            found = True
            for char in d1.keys():
                if d1[char] != d2[char]:
                    found = False
                    break
            if found:
                return True
            d2[s2[l]] -= 1
            l += 1
        return False
            
            
            