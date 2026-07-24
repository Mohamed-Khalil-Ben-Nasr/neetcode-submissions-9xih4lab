class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create adjacency list
        nodeToNeiCost = defaultdict(list)
        for x1, y1 in points:
            for x2, y2 in points:
                cost = abs(x1 - x2) + abs(y1 - y2)
                nodeToNeiCost[(x1, y1)].append([(x2, y2), cost])
        # intialize structs for dijkstra
        x, y = points[0]
        minHeap = [[0, (x, y)]]
        heapq.heapify(minHeap)
        visited = set()
        # since we have to connect all points, doesnt matter where we start
        res = 0
        while minHeap:
            if len(visited) == len(points):
                break
            curCost, curPoint = heapq.heappop(minHeap)
            # already visited this node via its cheapest route
            if curPoint in visited:
                continue
            visited.add(curPoint)
            res += curCost
            for nei, cost in nodeToNeiCost[curPoint]:
                heapq.heappush(minHeap, [cost, nei])
        return res
            

