class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        def isAlpha(c: chr):
            if (
                (ord('a') <= ord(c) <= ord('z')) 
                or (ord('A') <= ord(c) <= ord('Z'))
                or  (ord('0') <= ord(c) <= ord('9'))
            ):
                return True
            return False
        
        while l<=r :
            while ((not isAlpha(s[l])) and (l < r)):
                l += 1
            while ((not isAlpha(s[r])) and (l < r)):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True