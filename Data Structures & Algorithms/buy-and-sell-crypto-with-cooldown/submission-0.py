class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # in a certain day i, we can only be in one of two states: buy or sell
        # include or explude + bounded options => 0/1 knapsack
        dp = {}
        def dfs(i, buy):
            if (i,buy) in dp:
                return dp[(i,buy)]

            # we cant buy or sell beyond the specified # of days
            if i >= len(prices):
                return 0

            dp[(i, buy)] = 0
            # if today, we dont own a stock and we are gonna buy
            if buy:
                # should we buy today
                buyToday = -prices[i] + dfs(i+1, False)

                # or should we wait and buy in the future
                waitToBuy = dfs(i+1, True)

                dp[(i, buy)] = max(buyToday, waitToBuy)
            else:
            # if today, we hold a stock and we can sell it
                # should we sell today => 1 day cooldown + sell the day after
                sellToday = prices[i] + dfs(i+2, True)

                # or should we wait and sell in the future
                waitToSell = dfs(i+1, False)

                dp[(i, buy)] = max(sellToday, waitToSell)
            return dp[(i, buy)]
        return dfs(0, True)