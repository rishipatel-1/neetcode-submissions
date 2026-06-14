import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for stone in stones:
            heap.append(-stone)

        heapq.heapify(heap)

        while len(heap) > 1:
            firstStone = heapq.heappop(heap)
            secondStone = heapq.heappop(heap)

            if firstStone != secondStone:
                heapq.heappush(heap,firstStone - secondStone )    

        return -heap[0] if heap else 0        

