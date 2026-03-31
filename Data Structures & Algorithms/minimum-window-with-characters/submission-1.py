class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for c in t:
            d[c] = 1 + d.get(c, 0)
        
        curr = {}
        l = 0
        res = ""
        # constraint: max length = 1000
        maxL = 1200
        haveWhatWeNeed = False
        for r in range(len(s)):
            if s[r] in d.keys():
                curr[s[r]] = 1 + curr.get(s[r], 0)
            
            i = 0
            for k in d.keys():
                currK = curr.get(k, 0)
                if d[k] <= currK:
                    i += 1
            if i == len(d):
                haveWhatWeNeed = True
                
            while haveWhatWeNeed:
                if (r-l+1) < maxL:
                    res = s[l:r+1]
                    maxL = len(res)
                if s[l] in d.keys():
                    curr[s[l]] -= 1
                    if curr[s[l]] < d[s[l]]:
                        haveWhatWeNeed = False
                l += 1
        
        return res
