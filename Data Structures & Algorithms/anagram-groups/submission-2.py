from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def createAnagram(s: str):
            d = [0] * 26
            for c in s:
                d[ord(c) - ord('a')] += 1
            return tuple(d)
        
        res = defaultdict(list)
        for s in strs:
            currAnagram = createAnagram(s)
            res[currAnagram].append(s)
        
        return list(res.values())
        
