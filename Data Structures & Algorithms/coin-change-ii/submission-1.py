class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {}

        def dfs(i, total):

            if total == amount:
                return 1

            if total > amount:
                return 0
                
            # No coins left to use
            if i == len(coins):
                return 0

            # Already solved this state
            if (i, total) in cache:
                return cache[(i, total)]

            # Take current coin or skip to next coin
            cache[(i, total)] = (
                dfs(i, total + coins[i]) +
                dfs(i + 1, total)
            )

            return cache[(i, total)]

        return dfs(0, 0)