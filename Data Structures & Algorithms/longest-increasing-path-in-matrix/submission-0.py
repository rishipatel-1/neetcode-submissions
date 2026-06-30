class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        memo = {}

        def dfs(row, col):

            if (row, col) in memo:
                return memo[(row, col)]

            longest = 1

            directions = [(1, 0), (-1, 0),(0, 1), (0, -1)]

            for dr, dc in directions:

                newRow = row + dr
                newCol = col + dc

                # Stay inside grid and move to a larger value
                if (
                    0 <= newRow < rows and
                    0 <= newCol < cols and
                    matrix[newRow][newCol] > matrix[row][col]
                ):
                    longest = max(longest, 1 + dfs(newRow, newCol))

            # Save answer for this cell
            memo[(row, col)] = longest
            return longest

        answer = 0

        for row in range(rows):
            for col in range(cols):
                answer = max(answer, dfs(row, col))

        return answer