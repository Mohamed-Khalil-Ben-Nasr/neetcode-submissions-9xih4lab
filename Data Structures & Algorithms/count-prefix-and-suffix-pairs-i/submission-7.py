class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1, s2):
            # is pref
            i = 0
            while i < len(s1):
                if s1[i] != s2[i]:
                    return False
                i += 1
            
            # is suf
            j = len(s1)-1
            k = len(s2)-1
            while j >= 0:
                if s1[j] != s2[k]:
                    return False
                j -= 1
                k -= 1
            
            return True

        
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i]) > len(words[j]):
                    continue
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        
        return res