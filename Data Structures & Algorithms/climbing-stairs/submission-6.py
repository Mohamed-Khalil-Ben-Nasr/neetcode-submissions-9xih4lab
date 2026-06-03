class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom-up iterative approach with tabulation
        mem = [-1] * (n+1)
        mem[0] = 1
        mem[1] = 1
        for i in range(2,n+1):
            mem[i] = mem[i-1] + mem[i-2]
        
        return mem[n]
            