import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = {}

        for source, destination, time in times:
            if source not in graph:
                graph[source] = []
            graph[source].append((destination, time))

        minHeap = [(0, k)]
        visited = set()
        maxTime = 0

        while minHeap:
            cost, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            maxTime = max(maxTime, cost)

            if node in graph:
                for neighbor, edgeCost in graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(minHeap, (cost + edgeCost, neighbor))

        if len(visited) == n:
            return maxTime

        return -1