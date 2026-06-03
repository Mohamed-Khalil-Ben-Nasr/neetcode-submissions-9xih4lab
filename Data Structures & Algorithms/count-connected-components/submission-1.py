from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjacency list
        nodeToNeighbors = defaultdict(list)
        for edge in edges:
            a, b = edge[0], edge[1]
            nodeToNeighbors[a].append(b)
            nodeToNeighbors[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in nodeToNeighbors[node]:
                dfs(nei)
            return
        
        res = 0
        for node in nodeToNeighbors:
            # dfs will be triggered when we start exploring the nodes of a new component
            # and add all of the vertices of the new component to the visited set
            if node not in visited:
                dfs(node)
                res += 1
        if len(visited) < n:
            res += n - len(visited)
            
        return res