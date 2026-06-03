class Solution:
    def climbStairs(self, n: int) -> int:
        # top-down recursive approach with memoization
        mem = [-1] * (n+1)
        def dfs(i):
            # to reach 0, its 1 way == 0 steps
            # to reach 1, its 1 way == 1 step
            if i <= 1:
                mem[i] = 1

            if mem[i] != -1:
                return mem[i]

            mem[i] = dfs(i-1) + dfs(i-2)
            return mem[i]
        dfs(n)
        print(mem)
        return mem[n]
            