from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None

        rows , cols = len(grid) , len(grid[0])

        queue = deque()

        INF = 2147483647

        directions =[[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            r , c = queue.popleft()

            for rowMove , colMove in directions:
                newRow = r + rowMove
                newCol = c + colMove

                if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == INF:
                    grid[newRow][newCol] = grid[r][c] + 1
                    queue.append((newRow, newCol))
                        




     
        