class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = { 0 : 1}

        curr_sum = 0

        count = 0


        for num in nums:

            curr_sum += num

            need = curr_sum - k

            if need in prefix:
                count += prefix[need]

            prefix[curr_sum] = prefix.get(curr_sum ,0 ) + 1

        return count    
        