class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # create adjacency list
        # O(n^2) time and space
        nodeToNeiCost = defaultdict(list)
        for x1, y1 in points:
            for x2, y2 in points:
                cost = abs(x1 - x2) + abs(y1 - y2)
                nodeToNeiCost[(x1, y1)].append([(x2, y2), cost])
        # intialize structs for PRIMS MST
        x, y = points[0]
        minHeap = [[0, (x, y)]]
        heapq.heapify(minHeap)
        visited = set()
        # since we have to connect all points, doesnt matter where we start
        res = 0
        # building the MST: O(n^2 * log(n))
        # we visit every node once => O(n)
        # every node is connected to all nodes => O(n)
        # when we push and pop every node => O(log(heap_size)) = O(log(n**2)) = O(logn)
        while minHeap:
            # break after visiting all points
            if len(visited) == len(points):
                break
            curCost, curPoint = heapq.heappop(minHeap)
            # already visited this node by adding the cheapest edge
            # that connects it to the current tree
            if curPoint in visited:
                continue
            visited.add(curPoint)
            res += curCost
            for nei, cost in nodeToNeiCost[curPoint]:
                heapq.heappush(minHeap, [cost, nei])
        return res
            

