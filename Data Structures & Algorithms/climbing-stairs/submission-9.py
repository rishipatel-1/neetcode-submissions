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

        one = 1

        two = 1


        for i in range(n - 1):

            temp = one

            one = one + two

            two = temp


        return one