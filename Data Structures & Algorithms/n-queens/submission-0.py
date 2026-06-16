class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:

        cols = set()

        posDiag = set()      # r + c

        negDiag = set()      # r - c


        board = [["."] * n for _ in range(n)]

        res = []


        def dfs(r):


            # Base Case

            if r == n:

                copy = ["".join(row) for row in board]

                res.append(copy)

                return


            # Choices

            for c in range(n):


                # Unsafe ?

                if (

                    c in cols

                    or

                    (r + c) in posDiag

                    or

                    (r - c) in negDiag

                ):

                    continue


                # Choose

                cols.add(c)

                posDiag.add(r + c)

                negDiag.add(r - c)

                board[r][c] = "Q"


                # Go Deeper

                dfs(r + 1)


                # Undo

                cols.remove(c)

                posDiag.remove(r + c)

                negDiag.remove(r - c)

                board[r][c] = "."


        dfs(0)

        return res