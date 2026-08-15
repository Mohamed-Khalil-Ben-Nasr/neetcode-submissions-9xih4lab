class Solution:
    def validPalindrome(self, s: str) -> bool:
        # try all options of deletion
        for i in range(len(s)):
            cur = s[:i] + s[i+1:]
            l, r = 0, len(cur)-1
            while l < r:
                if cur[l] != cur[r]:
                    break
                l += 1
                r -= 1
            if not (l<r):
                return True
        return False