class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {}
        visited = set()
        count = 0

        for node in range(n):
            graph[node] = []

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)


        def dfs(node):
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1

        return count                

