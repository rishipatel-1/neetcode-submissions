class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        rows = len(s1)
        cols = len(s2)

        dp = [[False] * (cols + 1) for _ in range(rows + 1)]

        dp[rows][cols] = True

        for i in range(rows, -1, -1):
            for j in range(cols, -1, -1):

                # Try taking next character from s1
                if i < rows and s1[i] == s3[i + j]:
                    dp[i][j] |= dp[i + 1][j]

                # Try taking next character from s2
                if j < cols and s2[j] == s3[i + j]:
                    dp[i][j] |= dp[i][j + 1]

        return dp[0][0]