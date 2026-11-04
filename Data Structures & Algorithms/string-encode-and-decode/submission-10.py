class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            l = int(s[i:j])
            i = j + 1
            cur = s[i: i+l]
            res.append(cur)
            i += l
        return res