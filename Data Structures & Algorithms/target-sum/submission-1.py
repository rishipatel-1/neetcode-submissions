class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # dp[i] stores: sum -> number of ways
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        # Using 0 numbers, there is one way to make sum 0
        dp[0][0] = 1

        # Process one number at a time
        for i in range(len(nums)):

            # Try every sum we can currently make
            for cur_sum, count in dp[i].items():

                # Put '+' before current number
                dp[i + 1][cur_sum + nums[i]] += count

                # Put '-' before current number
                dp[i + 1][cur_sum - nums[i]] += count

        return dp[len(nums)][target]