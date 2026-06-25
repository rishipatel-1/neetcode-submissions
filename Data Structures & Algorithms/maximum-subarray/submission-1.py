# Kadane's Algorithm is a greedy algorithm used to find the maximum sum of a contiguous subarray in O(n) time.

# At every index, it decides whether to:
# 1. Continue the current subarray.
# 2. Start a new subarray.

# If the current running sum becomes negative, it is discarded because it can only decrease any future subarray sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]

        currSum = 0

        for num in nums:
            if currSum < 0:
                currSum = 0

            currSum += num
            maxSum = max(maxSum,currSum)

        return maxSum