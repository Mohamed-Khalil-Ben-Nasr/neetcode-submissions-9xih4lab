class Solution:

    def encode(self, strs: List[str]) -> str:
        # each string will have form: charCount#actualString/
        res = ""
        for i,s in enumerate(strs):
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            curL = 0
            while s[j] != "#":
                j += 1
            curL = int(s[i:j])
            curS = s[j+1: j+1 + curL]
            res.append(curS)
            i = j+1+ curL


        return res