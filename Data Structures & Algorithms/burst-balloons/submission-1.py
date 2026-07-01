class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        memo = {}

        def dfs(left, right):

            if left + 1 == right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            coins = 0

            for i in range(left + 1, right):

                current = (
                    nums[left] * nums[i] * nums[right]
                    + dfs(left, i)
                    + dfs(i, right)
                )

                coins = max(coins, current)

            memo[(left, right)] = coins
            return coins

        return dfs(0, len(nums) - 1)