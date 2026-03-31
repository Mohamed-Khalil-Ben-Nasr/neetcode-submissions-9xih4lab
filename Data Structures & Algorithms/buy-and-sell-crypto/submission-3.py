class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while r < len(prices):
            # check if this is profitable
            if prices[l] < prices[r]:
                cur = prices[r] - prices[l]
                res = max(res, cur)
            else:
                # that means we found a lower buying price
                # "buy low, sell high"
                l = r
            r += 1
        
        return res