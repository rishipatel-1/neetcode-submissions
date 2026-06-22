class Solution:

    # dp[i] = Number of ways to reach stair i
    #
    # To reach stair i:
    # We can come from i-1 or i-2
    #
    # Recurrence:
    # dp[i] = dp[i-1] + dp[i-2]
    #
    # Build answers from smaller stairs to bigger stairs.
    #
    # Time : O(n)
    # Space: O(n)

    def climbStairs(self, n: int) -> int:

        if n <= 2:

            return n


        dp = []

        for i in range(n + 1):

            dp.append(0)


        dp[1] = 1

        dp[2] = 2


        for i in range(3, n + 1):

            dp[i] = dp[i - 1] + dp[i - 2]


        return dp[n]