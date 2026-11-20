class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeToNeighbors = defaultdict(list)
        for a, b in edges:
            nodeToNeighbors[a].append(b)
            nodeToNeighbors[b].append(a)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in nodeToNeighbors[node]:
                if nei not in visited:
                    dfs(nei)
            
            return
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
            
        return res