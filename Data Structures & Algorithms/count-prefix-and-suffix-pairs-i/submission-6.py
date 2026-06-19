class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1, s2):
            return s2.startswith(s1) and s2.endswith(s1)
        
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i]) > len(words[j]):
                    continue
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        
        return res