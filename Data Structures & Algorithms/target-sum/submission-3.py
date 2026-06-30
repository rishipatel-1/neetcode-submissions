class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)

        if abs(target) > total:
            return 0

        if (target + total) % 2 != 0:
            return 0

        pos = (target + total) // 2

        dp = [0] * (pos + 1)

        # One way to make sum 0 (choose nothing)
        dp[0] = 1

        # Build subset sums
        for num in nums:

            # Traverse backwards so each number is used only once
            for s in range(pos, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[pos]