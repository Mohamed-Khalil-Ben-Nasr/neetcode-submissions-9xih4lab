class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        l = 0
        m = 0
        cur = 0
        s = set()
        for r in range(len(st)):
            while st[r] in s:
                s.remove(st[l])
                l += 1
            s.add(st[r])
            cur = r - l + 1
            m = max(m,cur)
        return m