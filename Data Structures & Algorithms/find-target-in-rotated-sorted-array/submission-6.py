class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            # target found
            if nums[mid] == target:
                return mid

            # LEFT SIDE SORTED
            if nums[l] <= nums[mid]:

                # target inside left sorted portion
                if nums[l] <= target < nums[mid]:

                    r = mid - 1

                else:
                    l = mid + 1

            # RIGHT SIDE SORTED
            else:

                # target inside right sorted portion
                if nums[mid] < target <= nums[r]:

                    l = mid + 1

                else:
                    r = mid - 1

        return -1