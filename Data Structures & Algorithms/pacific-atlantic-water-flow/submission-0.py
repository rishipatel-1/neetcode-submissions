class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows , cols = len(heights) , len(heights[0])

        pacific = set()

        atlantic = set()

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r,c,visited):

            visited.add((r,c))

            for rowMove , colMove in directions:
                newRow = r + rowMove
                newCol = c + colMove

                if 0 <= newRow < rows and 0 <= newCol < cols and (newRow,newCol) not in visited and heights[newRow][newCol] >= heights[r][c]:
                    dfs(newRow, newCol, visited)

        for r in range(rows):
            dfs(r,0,pacific)

        for c in range(cols):
            dfs(0,c,pacific)

        for r in range(rows):
            dfs(r,cols - 1, atlantic)

        for c in range(cols):
            dfs(rows-1, c, atlantic)        

        answer = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    answer.append([r,c])


        return answer            


        