class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:

            # Partition index in A
            i = (l + r) // 2

            j = half - i - 2

            # Values around partition in A
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")

            # Values around partition in B
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # Correct partition found
            if Aleft <= Bright and Bleft <= Aright:

                # Odd total length
                if total % 2:
                    return min(Aright, Bright)

                # Even total length
                return (
                    max(Aleft, Bleft) +
                    min(Aright, Bright)
                ) / 2

            # Need to move partition left
            elif Aleft > Bright:
                r = i - 1

            # Need to move partition right
            else:
                l = i + 1