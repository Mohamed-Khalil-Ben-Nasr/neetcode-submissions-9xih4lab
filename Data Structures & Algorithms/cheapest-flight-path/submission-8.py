class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for i in range(n)]
        prices[src] = 0
        # bellman-ford: k+1 relaxation rounds
        # at each ith relaxation round, we found the cheapest path from source to the node with at most i edges
        for i in range(k+1):
            tmp = prices.copy()
            for s,d,p in flights:
                if prices[s] == float("inf"):
                    continue
                # relaxation
                if prices[s] + p < tmp[d]:
                    tmp[d] = prices[s] + p
            prices = tmp

        return prices[dst] if prices[dst] != float("inf") else -1