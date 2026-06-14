class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for point in points:
            x , y = point 

            dist = x*x + y*y

            heapq.heappush(heap, (-dist, point))

            if len(heap) > k:
                heapq.heappop(heap)


        res = []

        for dist, point in heap:
            res.append(point)

        return res            
        