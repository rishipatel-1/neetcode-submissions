class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # left and right pointers
        l, r = 0, len(nums) - 1

        # normal binary search loop
        while l <= r:

            # middle index
            mid = (l + r) // 2

            # target found
            if nums[mid] == target:
                return mid

            # -----------------------------------
            # CHECK IF LEFT SIDE IS SORTED
            # -----------------------------------

            if nums[l] <= nums[mid]:

                # check if target exists inside left sorted portion
                if nums[l] <= target < nums[mid]:

                    # move to left side
                    r = mid - 1

                else:
                    # target must be on right side
                    l = mid + 1

            # -----------------------------------
            # OTHERWISE RIGHT SIDE IS SORTED
            # -----------------------------------

            else:

                # check if target exists inside right sorted portion
                if nums[mid] < target <= nums[r]:

                    # move to right side
                    l = mid + 1

                else:
                    # target must be on left side
                    r = mid - 1

        # target not found
        return -1