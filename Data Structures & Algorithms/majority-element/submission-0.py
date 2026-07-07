class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        bucket = [[] for i in range(len(nums)+1)]  

        for num , freq in count.items():
            bucket[freq].append(num)  

        for i in range(len(bucket)-1,-1,-1):
            if bucket[i]:
                return bucket[i][0]    
        
