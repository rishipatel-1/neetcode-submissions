class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP table with one extra row and column for the base case
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        # Build answer from the end of both strings
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # Characters match → take it and move diagonally
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # Characters don't match → skip one character
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]