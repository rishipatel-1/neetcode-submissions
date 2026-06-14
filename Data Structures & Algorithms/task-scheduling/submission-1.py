import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks, n):

        # Step 1: Count frequencies

        count = {}

        for task in tasks:

            count[task] = count.get(task, 0) + 1


        # Step 2: Build Max Heap using negatives

        heap = []

        for task in count:

            heap.append(-count[task])

        heapq.heapify(heap)


        # Step 3: Cooldown Queue

        q = deque()

        time = 0


        # Step 4: Run until everything finishes

        while heap or q:

            time += 1


            # Execute a task if available

            if heap:

                cnt = heapq.heappop(heap)

                cnt += 1      # because negative frequencies

                # Still some occurrences left

                if cnt:

                    q.append((cnt, time + n))


            # Cooldown finished?

            if q and q[0][1] == time:

                cnt, available_time = q.popleft()

                heapq.heappush(heap, cnt)


        return time