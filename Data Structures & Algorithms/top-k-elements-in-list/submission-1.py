class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n,0) + 1


        bucket = []
        for _ in range(len(nums)+1):
            bucket.append([])
        for num , freq in count.items():
            bucket[freq].append(num)


        result = []

        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result            



        