import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = set()

        minHeap = [(grid[0][0], 0, 0)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        while minHeap:
            time, row, col = heapq.heappop(minHeap)

            if (row, col) in visited:
                continue

            visited.add((row, col))

            if row == n - 1 and col == n - 1:
                return time

            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc

                if 0 <= newRow < n and 0 <= newCol < n and (newRow, newCol) not in visited:
                    newTime = max(time, grid[newRow][newCol])
                    heapq.heappush(minHeap, (newTime, newRow, newCol))