class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        rows = len(s)
        cols = len(t)

        # dp[i][j] = Number of ways to build t[j:] using s[i:]
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Empty target can always be formed
        for i in range(rows + 1):
            dp[i][cols] = 1

        # Build from bottom-right
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):

                # Skip current character
                dp[i][j] = dp[i + 1][j]

                # Take current character if it matches
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]