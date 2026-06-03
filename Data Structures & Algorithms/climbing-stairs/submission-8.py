class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom-up iterative approach optimized without tabulation
        prev1 = 1
        prev2 = 1
        cur = 1
        for i in range(2,n+1):
            cur = prev1 + prev2
            prev1 = prev2
            prev2 = cur
        
        return cur
            