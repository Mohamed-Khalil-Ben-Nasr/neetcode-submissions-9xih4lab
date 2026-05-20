class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        closeToOpen = {}
        closeToOpen['}'] = '{'
        closeToOpen[']'] = '['
        closeToOpen[')'] = '('

        for c in s:
            if c in closeToOpen:
                if len(res) == 0:
                    return False

                if res[-1] == closeToOpen[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        
        if len(res) != 0:
            return False
        else: 
            return True