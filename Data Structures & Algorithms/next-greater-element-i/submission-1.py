class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []

        nextGreater = {}

        for num in nums2:

            while stack and num > stack[-1]:

                smaller = stack.pop()

                nextGreater[smaller] = num

            stack.append(num)

        while stack:

            nextGreater[stack.pop()] = -1

        res = []

        for num in nums1:
            res.append(nextGreater[num])

        return res