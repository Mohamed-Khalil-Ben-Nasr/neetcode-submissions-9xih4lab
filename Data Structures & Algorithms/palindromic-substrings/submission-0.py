class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def numPalindromes(i):
            p = 0
            # num odd palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                p += 1
                l -= 1
                r += 1

            # num even palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                p += 1
                l -= 1
                r += 1
            return p

        for i in range(len(s)):
            res += numPalindromes(i)
        
        return res
