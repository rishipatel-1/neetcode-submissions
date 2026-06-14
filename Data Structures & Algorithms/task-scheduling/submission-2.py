import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            count[task] = count.get(task,0) + 1

        heap = []

        for task in count:
            heap.append(-count[task])


        heapq.heapify(heap)
        
        q = deque()

        time = 0

        while q or heap:

            time+=1

            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1

                if cnt:
                    q.append((cnt,time+n))

            if q and q[0][1] == time:
                cnt , available_time = q.popleft()
                heapq.heappush(heap, cnt)



        return time        

                
                        

                

                

            
            

        
            
        
            
        