#We process the array from left to right while maintaining a running (prefix) sum. At every element, we assume the current index is the end of a possible subarray and ask: "What previous prefix sum would I need to remove so that the remaining 
#subarray sums to k?" That required value is current_prefix - k.
# We store all previously seen prefix sums and how many times they've occurred in a HashMap. If the required prefix sum has been seen before, 
#each occurrence represents a different valid starting point for a subarray ending at the current index, so we add its frequency to our answer. Finally, we store the current prefix sum in the HashMap so future elements can use it.


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
        