class Solution:
    def longestPalindrome(self, s: str) -> str:
        # the trick is to realize that we need to detect both odd and even
        # length palindromes
        # => detect both "aba" and "aab" then pick max
        # => expand accordingly
        res = ""
        def palindrome(i, odd):
            nonlocal res
            left, right = i, i+1
            if odd:
                right = i
            # while in bounds and the extremities match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(res):
                    res = s[left:right+1]
                left -= 1
                right += 1

        for i in range(len(s)):
            # odd 
            palindrome(i, True)

            # even
            palindrome(i, False)
        
        return res