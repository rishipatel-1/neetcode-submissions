class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)

        parent = {}

        for node in range(1, n+1):
            parent[node] = node

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x        

        def union(a,b):
            parentA = find(a)
            parentB = find(b)

            parent[parentB] = parentA
                
        for a,b in edges:
            if find(a) == find(b):
                return [a,b]
            union(a,b)    

        