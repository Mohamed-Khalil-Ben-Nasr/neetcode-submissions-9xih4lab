class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodeToNeis = defaultdict(list)
        for u,v,t in times:
            nodeToNeis[u].append([t,v])
        
        visited = set()
        minHeap = [[0, k]]
        heapq.heapify(minHeap)
        res = 0
        while minHeap:
            curCost, curNode = heapq.heappop(minHeap)
            if curNode in visited:
                continue
            visited.add(curNode)
            # once the source node is reached, the signal is propagated to all 
            # neighbor nodes via the outgoing edges simultaneously
            # => time taken = max cost to reach last node that we can visit
            res = max(res, curCost)
            for cost, node in nodeToNeis[curNode]:
                heapq.heappush(minHeap, [cost + curCost, node])  

        if len(visited) != n:
            return -1
        return res


        