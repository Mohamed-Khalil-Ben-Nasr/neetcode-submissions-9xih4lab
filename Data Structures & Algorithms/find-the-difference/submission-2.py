from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s)
        for c in t:
            # Characters not in s at all
            # or Characters that have been fully used up
            # ie s= "aa" and t = "aaa"
            if count[c] == 0:
                return c
            count[c] -= 1