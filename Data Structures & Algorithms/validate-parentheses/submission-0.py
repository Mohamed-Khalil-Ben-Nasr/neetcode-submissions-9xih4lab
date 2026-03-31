class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {}
        closeToOpen[')'] = '('
        closeToOpen[']'] = '['
        closeToOpen['}'] = '{'
        res = []
        for c in s:
            if c in closeToOpen.keys():
                if not res:
                    return False
                o = res.pop()
                if closeToOpen[c] != o:
                    return False
            else:
                res.append(c)
        
        return not res