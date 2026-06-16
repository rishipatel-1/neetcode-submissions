class Solution:

    def generateParenthesis(self, n):

        res = []

        stack = []


        def dfs(openN, closeN):

            # Base Case
            if openN == closeN == n:

                res.append("".join(stack))

                return


            # Add '('
            if openN < n:

                stack.append("(")

                dfs(openN + 1, closeN)

                stack.pop()


            # Add ')'
            if closeN < openN:

                stack.append(")")

                dfs(openN, closeN + 1)

                stack.pop()


        dfs(0,0)

        return res