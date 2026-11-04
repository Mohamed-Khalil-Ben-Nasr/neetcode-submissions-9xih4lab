class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
                continue
            cur = prices[r] - prices[l]
            res = max(res, cur)
        return res