class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlph(c):
            if (ord('a') <= ord(c) <= ord('z')
            or ord('A') <= ord(c) <= ord('Z')
            or ord('0') <= ord(c) <= ord('9')):
                return True
            else:
                return False
        
        i, j = 0, len(s)-1
        while i < j:
            while i<j and not isAlph(s[i]):
                i += 1
            while i<j and not isAlph(s[j]):
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        
        return True
