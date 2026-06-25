class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):

            dp[i][0] = True

        for i in range(len(nums) - 1, -1, -1):

            for currTarget in range(1, target + 1):

                skip = dp[i + 1][currTarget]

                take = False

                if currTarget >= nums[i]:

                    take = dp[i + 1][currTarget - nums[i]]

                dp[i][currTarget] = take or skip

        return dp[0][target]