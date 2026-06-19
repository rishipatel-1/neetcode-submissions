from collections import deque


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        freshOranges = 0
        minutes = 0
        directions = [[1,0],[-1,0] ,[0,1],[0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshOranges += 1

        while queue and freshOranges > 0:
            queueSize = len(queue)

            for i in range(queueSize):
                r, c = queue.popleft()

                for rowMove, colMove in directions:
                    newRow = r + rowMove
                    newCol = c + colMove

                    if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        freshOranges -= 1
                        queue.append((newRow, newCol))

            minutes += 1

        if freshOranges == 0:
            return minutes


        return -1