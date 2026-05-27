class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        res = nums[0]

        while l <= r:

            # if current portion already sorted
            if nums[l] < nums[r]:

                # leftmost is minimum
                res = min(res, nums[l])

                break

            m = (l + r) // 2

            # update current minimum
            res = min(res, nums[m])

            # left portion sorted
            if nums[m] >= nums[l]:

                # minimum must be right side
                l = m + 1

            else:
                # minimum in left side
                r = m - 1

        return res