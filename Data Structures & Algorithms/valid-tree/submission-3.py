from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # In an undirected graph, for checking tree validity you can start DFS from any node. 
        # If the graph is a valid tree, starting from any node will reach all others. 
        # If it's not, you'll detect a cycle or miss nodes regardless of where you start.

        # a tree is only valid if:
        # - no cycles 
        # - all vertices are connected ( no disconnected components )
        
        # create adjacency map
        nodeToNeighbors = defaultdict(list)
        for edge in edges:
            a, b = edge[0], edge[1]
            nodeToNeighbors[a].append(b)
            nodeToNeighbors[b].append(a)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in nodeToNeighbors[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

       
        # if cycle detected
        if not dfs(0, -1):
            return False
        
        # if # visited nodes < # keys
        # => we didnt visit all the nodes 
        # => disconnected edges
        # => forst
        if len(visited) != n:
            return False
        
        return True
        
