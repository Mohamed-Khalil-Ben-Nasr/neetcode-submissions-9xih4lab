class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        p = 0
        for sell in range(len(prices)):
            print("sell: ", sell)
            print("buy: ", buy)
            p = max(p, prices[sell] - prices[buy])
            print(p)
            if prices[buy] > prices[sell]:
                buy = sell
        
        return p
        
