class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        missing = n

        for i in range(n):
            missing ^= i
            missing ^= nums[i]

        return missing