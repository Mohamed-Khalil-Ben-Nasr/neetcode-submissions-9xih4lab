class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # keep track of the min val currently in the stack
        # when we add the new element
        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            self.stack.append([val, min(val, self.stack[-1][1])])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
