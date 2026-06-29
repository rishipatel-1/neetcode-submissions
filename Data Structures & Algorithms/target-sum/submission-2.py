class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)

        # Impossible to reach target
        if abs(target) > total:
            return 0

        # Positive subset sum must be an integer
        if (target + total) % 2 != 0:
            return 0

        # Sum we need to form using a subset
        pos = (target + total) // 2

        # Ways to make every sum from 0 to pos
        dp = [0] * (pos + 1)

        # One way to make sum 0 (choose nothing)
        dp[0] = 1

        # Build subset sums
        for num in nums:

            # Traverse backwards so each number is used only once
            for s in range(pos, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[pos]