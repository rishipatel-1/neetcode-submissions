class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()

        postDiag = set()

        negDiag = set()

        board = []

        for i in range(n):
            rows = ["."] * n
            board.append(rows)

        res = []


        def dfs(row):

            if row == n:
                copy = []
                for r in board:
                    copy.append("".join(r))
                res.append(copy)
                return

            for col in range(n):

                if col in cols or (row + col) in postDiag or (row-col) in negDiag :
                    continue

                cols.add(col)
                postDiag.add(row + col)
                negDiag.add(row - col)
                board[row][col] = "Q"


                dfs(row+1)

                cols.remove(col)
                postDiag.remove(row + col)
                negDiag.remove(row - col)
                board[row][col] = "."

        dfs(0)

        return res        
                    



                
                    
        
                    


                

        
            
            
        