class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Skip today and move to tomorrow
            cooldown = dfs(i + 1, buying)

            if buying:
                # Buy today or skip
                buy = dfs(i + 1, False) - prices[i]
                dp[(i, buying)] = max(cooldown, buy)

            else:
                # Sell today (cooldown tomorrow) or keep holding
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, buying)] = max(cooldown, sell)

            return dp[(i, buying)]

        return dfs(0, True)