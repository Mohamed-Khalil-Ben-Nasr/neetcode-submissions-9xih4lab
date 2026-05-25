class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # threshold crossing intuition:
        # "have" will only be incremented if ds[s[r]] == dt[s[r]]
        # the condition wont be triggered again when ds[s[r]] > dt[s[r]]
        # so no need to have a set
        dt = {}
        for c in t:
            dt[c] = 1 + dt.get(c,0)
        
        need = len(dt.keys())
        have = 0
        res = ""
        m = float("inf")
        l = 0
        ds = {}
        for r in range(len(s)):
            ds[s[r]] = 1 + ds.get(s[r],0)
            if s[r] in dt and ds[s[r]] == dt[s[r]]:
                have += 1
    
            # if we have all the needed letters
            while have == need:
                if (r - l + 1) < m:
                    res = s[l:r+1]
                    m = r - l + 1
                ds[s[l]] -= 1
                if s[l] in dt and ds[s[l]] < dt[s[l]]:
                    have -= 1
                l += 1
        return res

                   
