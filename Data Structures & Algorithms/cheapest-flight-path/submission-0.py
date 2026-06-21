import heapq


class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = {}

        for i in range(n):
            graph[i] = []

        for start, end, price in flights:
            graph[start].append((end, price))

        minHeap = [(0, src, 0)]
        best = {}

        while minHeap:
            cost, city, stops = heapq.heappop(minHeap)

            if stops > k + 1:
                continue

            if city == dst:
                return cost

            if (city, stops) in best and best[(city, stops)] <= cost:
                continue

            best[(city, stops)] = cost

            for neighbour, price in graph[city]:
                heapq.heappush(minHeap,(cost + price, neighbour, stops + 1))

        return -1