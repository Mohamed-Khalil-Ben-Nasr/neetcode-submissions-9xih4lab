class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid graph => no cycles + no disconnected components

        nodeToNeighbors = defaultdict(list)
        for a, b in edges:
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
        
        valid = dfs(0, -1)
        return valid and (len(visited) == n
)