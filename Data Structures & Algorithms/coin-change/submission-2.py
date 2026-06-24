class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(amount):
            if amount in memo:
                return memo[amount]

            if amount == 0:
                return 0

            if amount < 0:
                return float("inf")  

            minimun = float("inf")

            for coin in coins:
                minimun = min(minimun , 1 + dfs(amount - coin))

            memo[amount] = minimun    

            return minimun      

        answer = dfs(amount)

        if answer == float("inf"):
           return -1

        return answer
         



        