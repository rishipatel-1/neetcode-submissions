class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:

        cols = set()          # occupied columns

        posDiag = set()       # occupied r+c diagonals

        negDiag = set()       # occupied r-c diagonals


        board = [["."] * n for _ in range(n)]

        res = []


        def dfs(row):

            # Base Case

            if row == n:

                copy = []

                for r in board:

                    copy.append("".join(r))

                res.append(copy)

                return


            # Choices

            for col in range(n):


                # Unsafe ?

                if (

                    col in cols

                    or

                    (row + col) in posDiag

                    or

                    (row - col) in negDiag

                ):

                    continue


                # Choose

                cols.add(col)

                posDiag.add(row + col)

                negDiag.add(row - col)

                board[row][col] = "Q"


                # Go Deeper

                dfs(row + 1)


                # Undo

                cols.remove(col)

                posDiag.remove(row + col)

                negDiag.remove(row - col)

                board[row][col] = "."


        dfs(0)

        return res