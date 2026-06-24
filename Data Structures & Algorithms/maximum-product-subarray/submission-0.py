class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result = max(nums)

        currMax = 1
        currMin = 1

        for num in nums:

            tempMax = max(num, currMax * num, currMin * num)
            tempMin = min(num, currMax * num, currMin * num)

            currMax = tempMax
            currMin = tempMin

            result = max(result, currMax)

        return result