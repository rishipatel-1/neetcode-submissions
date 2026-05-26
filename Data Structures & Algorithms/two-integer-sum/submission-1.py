class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i , num in enumerate(nums):
            patner = target - num
            if patner in seen:
                return [seen[patner],i]
            seen[num] = i
        