class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i <= 3:
                return i

            memo[i] = dfs(i-1) + dfs(i-2)

            return memo[i]      

        return dfs(n)
        