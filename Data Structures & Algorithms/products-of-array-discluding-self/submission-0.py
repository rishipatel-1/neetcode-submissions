class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [1] * n

        left = 1
        for i in range(n):
            result[i] = left
            left = left * nums[i]
            
        right = 1 
        for i in range(n-1 , -1 , -1):
            result[i] = result[i] * right
            right = right * nums[i]


        return result        
        