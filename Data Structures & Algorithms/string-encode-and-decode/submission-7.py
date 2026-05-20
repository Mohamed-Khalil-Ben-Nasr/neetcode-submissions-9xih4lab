class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += str(l) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        l = len(s)
        res = []
        i = 0
        while i < l:
            # start from the first digit of the current string's length
            currL = ""
            while s[i] != '#':
                currL += s[i]
                i += 1
            currL = int(currL)
            # avoid the delimiter and start from the first char in the string
            i += 1
            res.append(s[i: i+currL])
            i += currL

        return res