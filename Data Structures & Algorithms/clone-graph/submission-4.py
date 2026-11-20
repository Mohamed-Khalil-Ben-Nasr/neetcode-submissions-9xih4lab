"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        # store the clones so that we dont keep creating clones indefinitely
        # O(V+E)
        # each node is cloned once and each neighbor is explored once (each adjacency entry / edge is explored once)
        def dfs(node):
            if not node:
                return None

            if node.val in clones:
                return clones[node.val]
            
            clone = Node(node.val)
            clones[node.val] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone
        
        return dfs(node)