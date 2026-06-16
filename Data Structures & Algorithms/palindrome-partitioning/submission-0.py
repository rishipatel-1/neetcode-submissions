class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        part = []


        def isPali(s, l, r):

            while l < r:

                if s[l] != s[r]:

                    return False

                l += 1

                r -= 1

            return True


        def dfs(i):

            # Base Case

            if i >= len(s):

                res.append(part.copy())

                return


            # Choices

            for j in range(i, len(s)):


                # Take s[i:j+1]

                if isPali(s, i, j):


                    # Choose

                    part.append(s[i:j+1])


                    # Go Deeper

                    dfs(j + 1)


                    # Undo

                    part.pop()


        dfs(0)

        return res