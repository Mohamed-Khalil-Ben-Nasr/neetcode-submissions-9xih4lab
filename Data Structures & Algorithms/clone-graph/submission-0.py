"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        originalToClone = {}

        def dfs(root):
            nonlocal originalToClone
            # base cases
            if not root:
                return None

            # return the clone if root was already visited
            if root in originalToClone:
                return originalToClone[root]
            
            # create new mapping
            originalToClone[root] = Node(val = root.val)

            # visit all neighbors recursively via dfs
            for i in range(len(root.neighbors)):
                neighborClone = dfs(root.neighbors[i])
                if neighborClone != None:
                    originalToClone[root].neighbors.append(neighborClone)

            return originalToClone[root]
        
        return dfs(node)