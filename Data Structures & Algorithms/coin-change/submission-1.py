class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(amount):
            if amount in memo:
                return memo[amount]

            if amount == 0:
                return 0

            if amount < 0:
                return float("infinity")  

            minimun = float("infinity")

            for coin in coins:
                minimun = min(minimun , 1 + dfs(amount - coin))

            memo[amount] = minimun    

            return minimun      

        answer = dfs(amount)

        if answer == float("infinity"):
           return -1

        return answer
         



        