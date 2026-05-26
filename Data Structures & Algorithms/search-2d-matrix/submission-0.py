class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        # STEP 1: Find correct row
        while top <= bottom:

            midRow = (top + bottom) // 2

            rowFirst = matrix[midRow][0]
            rowLast = matrix[midRow][-1]

            if target > rowLast:
                top = midRow + 1

            elif target < rowFirst:
                bottom = midRow - 1

            else:

                left = 0
                right = cols - 1

                # STEP 2: Binary search inside row
                while left <= right:

                    mid = (left + right) // 2

                    value = matrix[midRow][mid]

                    if target > value:
                        left = mid + 1

                    elif target < value:
                        right = mid - 1

                    else:
                        return True

                return False

        return False