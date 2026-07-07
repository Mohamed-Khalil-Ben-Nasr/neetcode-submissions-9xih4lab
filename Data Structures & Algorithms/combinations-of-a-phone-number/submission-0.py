class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digitToChars = {}
        digitToChars['2'] = ['a','b','c']
        digitToChars['3'] = ['d', 'e', 'f']
        digitToChars['4'] = ['g', 'h', 'i']
        digitToChars['5'] = ['j', 'k', 'l']
        digitToChars['6'] = ['m', 'n', 'o']
        digitToChars['7'] = ['p', 'q', 'r', 's']
        digitToChars['8'] = ['t','u','v']
        digitToChars['9'] = ['w', 'x', 'y', 'z']
        res = []
        combo = []
        def dfs(i):
            if i >= len(digits):
                res.append("".join(combo.copy()))
                return
            for char in digitToChars[digits[i]]:
                combo.append(char)
                dfs(i+1)
                combo.pop()
            return
        dfs(0)
        return res
