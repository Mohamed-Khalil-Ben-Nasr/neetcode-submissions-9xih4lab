class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(o, combo, stack):
            # success
            if len(combo) == n * 2 and not stack:
                res.append("".join(combo.copy()))
                return
            
            # failure
            if len(combo) == n*2:
                return

            # 2 branches in the decision tree:
            # add opening paranthesis
            if o > 0:
                combo.append("(")
                stack.append("(")
                dfs(o-1, combo, stack)
                # reset only after visiting this branch
                combo.pop()
                stack.pop()
            
            # add closing paranthesis
            # go down this branch only when it results in a valid combo
            if stack and stack[-1] == "(":
                stack.pop()
                combo.append(")")
                dfs(o, combo, stack)
                # reset after visiting this branch
                stack.append("(")
                combo.pop()
                
            return
        dfs(n-1, ["("], ["("])
        return res

