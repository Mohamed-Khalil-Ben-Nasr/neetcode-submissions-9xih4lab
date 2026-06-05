from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = defaultdict(int)
        for c in t:
            dt[c] += 1
        need = len(dt.keys())
        have = 0
        l = 0
        res = ""
        resLen = float("inf")
        d = defaultdict(int)
        for r in range(len(s)):
            if s[r] in dt:
                d[s[r]] += 1
                if d[s[r]] == dt[s[r]]:
                    have += 1
            while l <= r and have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                if s[l] in d:
                    d[s[l]] -= 1
                    if d[s[l]] < dt[s[l]]:
                        have -= 1
                l += 1
        return res