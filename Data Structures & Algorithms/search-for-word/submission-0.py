class Solution:

    def exist(self, board, word):

        ROWS = len(board)
        COLS = len(board[0])

        visited = set()


        def dfs(r, c, i):

            if i == len(word):
                return True


            # Invalid cell
            if (
                r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                board[r][c] != word[i] or
                (r, c) in visited
            ):
                return False


            # Choose
            visited.add((r, c))


            # Explore 4 directions

            res = (

                dfs(r + 1, c, i + 1) or     # DOWN

                dfs(r - 1, c, i + 1) or     # UP

                dfs(r, c + 1, i + 1) or     # RIGHT

                dfs(r, c - 1, i + 1)        # LEFT

            )


            # Undo
            visited.remove((r, c))


            return res


        # Find starting character

        for r in range(ROWS):

            for c in range(COLS):

                if dfs(r, c, 0):

                    return True


        return False