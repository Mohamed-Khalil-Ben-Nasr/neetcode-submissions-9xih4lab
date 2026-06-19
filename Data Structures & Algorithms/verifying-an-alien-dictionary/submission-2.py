class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        i = 0
        for c in order:
            d[c] = i
            i += 1
        
        k = 0
        while k < len(words)-1:
            w1 = words[k]
            w2 = words[k+1]
            j = 0
            while j < len(w1):
                if (j >= len(w2)):
                    return False
                if d[w1[j]] < d[w2[j]]:
                    break
                if d[w1[j]] > d[w2[j]]:
                    return False
                j += 1
            k += 1
        
        return True