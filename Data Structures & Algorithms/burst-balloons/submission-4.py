class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        memo = {}

        def dfs(l, r):

            # No balloons left
            if l > r:
                return 0

            # Already solved
            if (l, r) in memo:
                return memo[(l, r)]

            best = 0

            # Try every balloon as the LAST balloon
            for i in range(l, r + 1):

                coins = (
                    nums[l - 1] * nums[i] * nums[r + 1]
                    + dfs(l, i - 1)
                    + dfs(i + 1, r)
                )

                best = max(best, coins)

            memo[(l, r)] = best
            return best

        return dfs(1, len(nums) - 2)