class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set()
        ops.add("+")
        ops.add("-")
        ops.add("/")
        ops.add("*")
        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                res = 0
                num2 = int(stack.pop())
                num1 = int (stack.pop())
                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num1 - num2
                elif token == "*":
                    res = num1 * num2
                else:
                    # truncate toward 0
                    # if num1 = -2.5 => int(num1) = -2
                    # if num1 = 2.5 => int(num1) = 2
                    res = int(num1 / num2)
                print(res)
                stack.append(str(res))
        return int(stack[-1])