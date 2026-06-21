import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        visited = set()

        minHeap = [(0,0)]

        totalcost = 0

        def distance(i,j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        while len(visited) < len(points):
            cost , point = heapq.heappop(minHeap)

            if point in visited:
                continue

            visited.add(point)

            totalcost += cost

            for nextPoint in range(len(points)):
                if nextPoint not in visited:
                    edgeCost = distance(point,nextPoint) 
                    heapq.heappush(minHeap, (edgeCost, nextPoint))

        return totalcost         