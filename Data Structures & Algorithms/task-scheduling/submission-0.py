import heapq
from collections import Counter, deque

class Solution:

    def leastInterval(self, tasks, n):

        count = Counter(tasks)

        heap = []

        for freq in count.values():

            heap.append(-freq)

        heapq.heapify(heap)

        q = deque()

        time = 0

        while heap or q:

            time += 1

            if heap:

                cnt = heapq.heappop(heap)

                cnt += 1

                if cnt:

                    q.append((cnt, time+n))

            if q and q[0][1] == time:

                cnt, available = q.popleft()

                heapq.heappush(heap, cnt)

        return time