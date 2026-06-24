class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        memo = {}

        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        def dfs(i, target):

            if (i,target) in memo:
                return memo[(i, target)]

            if target == 0:
                return True

            if i == len(nums) or target < 0:
                return False

            take = dfs(i+1 , target - nums[i])

            skip = dfs(i+1, target)

            memo[(i, target)] = skip or take

            return take or skip      

        return dfs(0,target)    
        