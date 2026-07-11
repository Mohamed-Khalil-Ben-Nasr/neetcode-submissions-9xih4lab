class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # disjoint-sets union-find algorithm can be represented with
        # sets, array, or linked list
        # this is the array solution
        # initialization
        # V = number of vertices = number of edges + 1
        # since 1 edge is added to form a cycle, we add +1
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [0 for i in range(n+1)]
    
        def find(i):
            # this find implementation includes path compression
            # parent of every node is root => find is O(1)
            if i != parent[i]:
               parent[i] = find(parent[i])
            return parent[i]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # same parent => alredy in same connected component 
            # => adding new edge forms a cycle
            if p1 == p2:
                return False
            # perform union
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1, n2]



