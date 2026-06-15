class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        res = []
        path = []

        def dfs(i, total):

            if total == target:
                res.append(path.copy())
                return

            if total > target or i == len(nums):
                return

            for j in range(i, len(nums)):

                if j > i and nums[j] == nums[j - 1]:
                    continue

                # TAKE
                path.append(nums[j])

                # Move to NEXT index
                dfs(j + 1, total + nums[j])

                # UNDO
                path.pop()


        dfs(0, 0)

        return res