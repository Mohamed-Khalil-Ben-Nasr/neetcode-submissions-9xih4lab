class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def createDict(s: str):
            d = defaultdict(int)
            for i in range(len(s)):
                d[s[i]] += 1
            return d
        
        d1 = createDict(s)
        d2 = createDict(t)

        return d1==d2

        
        