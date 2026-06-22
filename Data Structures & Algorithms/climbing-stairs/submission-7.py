class Solution:

    # dp[i] = Number of ways to reach stair i
    #
    # Recurrence:
    # dp[i] = dp[i-1] + dp[i-2]
    #
    # Save answers in memo so we don't calculate again.
    #
    # Time : O(n)
    # Space: O(n)

    def climbStairs(self, n: int) -> int:

        memo = {}

        def dfs(i):

            if i in memo:

                return memo[i]

            if i <= 2:

                return i

            memo[i] = dfs(i - 1) + dfs(i - 2)

            return memo[i]

        return dfs(n)