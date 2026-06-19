from collections import deque


class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid:
            return


        rows, cols = len(grid), len(grid[0])

        INF = 2147483647

        queue = deque()


        # Add all treasures to queue

        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == 0:

                    queue.append((r,c))


        while queue:

            r, c = queue.popleft()


            # Down

            nr = r + 1

            nc = c

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:

                grid[nr][nc] = grid[r][c] + 1

                queue.append((nr,nc))


            # Up

            nr = r - 1

            nc = c

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:

                grid[nr][nc] = grid[r][c] + 1

                queue.append((nr,nc))


            # Right

            nr = r

            nc = c + 1

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:

                grid[nr][nc] = grid[r][c] + 1

                queue.append((nr,nc))


            # Left

            nr = r

            nc = c - 1

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:

                grid[nr][nc] = grid[r][c] + 1

                queue.append((nr,nc))