from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        for c in s1:
            d1[c] += 1
        for i in range(0, len(s2)-len(s1)+1):
            d2 = defaultdict(int)
            for j in range(i, i+len(s1)):
                d2[s2[j]] += 1
            match = True
            for c in d2:
                if d2[c] != d1[c]:
                    match = False
            if match:
                return True
        return False

