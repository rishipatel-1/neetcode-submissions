class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {}
        visited = set()

        for node in range(n):
            graph[node] = []

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if neighbor in visited:
                   return False

                if dfs(neighbor, node) == False:
                    return False
                    
            return True

        if dfs(0, -1) == False:
            return False

        return len(visited) == n