class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramToStrings = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            anagramToStrings[sortedS].append(s)
        return list(anagramToStrings.values())