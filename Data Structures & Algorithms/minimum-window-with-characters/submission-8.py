class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        dt = defaultdict(int)
        for c in t:
            dt[c] += 1
        
        need = len(dt.keys())
        have = 0
        lenRes = float("inf")
        res = ""
        l = 0
        ds = defaultdict(int)
        for r in range(len(s)):
            if s[r] in dt:
                ds[s[r]] += 1
                if ds[s[r]] == dt[s[r]]:
                    have += 1
            
            while need == have:
                if (r - l + 1) < lenRes:
                    lenRes = r - l + 1
                    res = s[l: r+1]
                if s[l] in dt:
                    ds[s[l]] -= 1
                    if ds[s[l]] < dt[s[l]]:
                        have -= 1
                l += 1
        return res
                