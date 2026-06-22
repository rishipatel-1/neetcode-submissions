class Solution:

    # dp[i] depends only on:
    #
    # dp[i-1]
    # dp[i-2]
    #
    # So store only last two answers.
    #
    # Time : O(n)
    # Space: O(1)

    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 1

        for i in range(n-1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1    

