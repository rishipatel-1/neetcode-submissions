class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Last row has only one path to the destination
        row = [1] * n

        # Build the answer from bottom to top
        for i in range(m - 1):
            # Last column also has only one path
            newRow = [1] * n
            # Current cell = Right + Down
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            # Current row becomes the row below
            row = newRow

        return row[0]