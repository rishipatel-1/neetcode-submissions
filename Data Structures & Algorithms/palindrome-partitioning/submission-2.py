class Solution:

    def partition(self, s: str) -> List[List[str]]:

        res = []
        part = []

        def isPali(l, r):

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


            # Try all substrings starting at i
            for j in range(i, len(s)):

                # Check palindrome
                if isPali(i, j):

                    # Choose
                    part.append(s[i:j+1])

                    # Go deeper
                    dfs(j + 1)

                    # Undo
                    part.pop()


        dfs(0)

        return res