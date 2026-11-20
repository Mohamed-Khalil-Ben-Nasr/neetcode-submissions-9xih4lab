class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeToNeighbors = defaultdict(list)
        for a, b in edges:
            nodeToNeighbors[a].append(b)
            nodeToNeighbors[b].append(a)
        
        visited = set()
        processed = set()

        def dfs(node, parent):
            if node in processed:
                return True
            
            if node in visited:
                return False
            
            visited.add(node)
            for nei in nodeToNeighbors[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            processed.add(node)
            return True
        
        valid = dfs(0, -1)
        return valid and (len(processed) == n
)