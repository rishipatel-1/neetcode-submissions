class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        memo = {}

        def dfs(i, j):

            # Successfully built the target
            if j == len(t):
                return 1

            # Source finished before target
            if i == len(s):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            # Skip current character
            skip = dfs(i + 1, j)

            # Take current character if it matches
            take = 0
            if s[i] == t[j]:
                take = dfs(i + 1, j + 1)

            # Total ways = take + skip
            memo[(i, j)] = take + skip

            return memo[(i, j)]

        return dfs(0, 0)