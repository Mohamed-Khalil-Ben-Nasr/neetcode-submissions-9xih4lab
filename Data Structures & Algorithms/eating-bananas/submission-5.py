class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # len(piles) <= h
        # max k = max piles and min k = min piles
        minimum, maximum = 1, max(piles)
        res = maximum
        while minimum <= maximum:
            k = (minimum + maximum) // 2
            print("cur K ",k )
            curH = 0
            for i in range(len(piles)):
                # ceiling
                curH += (piles[i] + k - 1) // k
                print(curH)
            print("cur H ", curH)
            # this rate is too slow
            if curH > h:
                minimum = k + 1
                print("cur H is slow => minimum is ", minimum)
            # this rate is fast enough
            else:
                res = min(k, res)
                maximum = k - 1
                print("cur H is fast enough => max is ", maximum)
        return res
