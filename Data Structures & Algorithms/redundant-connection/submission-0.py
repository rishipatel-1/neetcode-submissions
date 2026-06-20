# solution one that is heavy time complex becuase for every edge we perform dfs

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = {}

        def dfs(source, target , visited):

            if source == target:
                return True

            visited.add(source)

            for neighbour in graph[source]:
                if neighbour not in visited:
                    if dfs(neighbour,target,visited):
                        return True
                    
            return False

        for a,b in edges:
            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []


            visited = set()

            if graph[a] and graph[b]:
                if dfs(a,b,visited):
                    return [a,b]

            graph[a].append(b)
            graph[b].append(a)        

                    
                    
                        
            

        

        